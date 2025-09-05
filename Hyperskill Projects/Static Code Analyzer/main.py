import os
import sys
import ast
import re


class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self, file_path):
        self.tree = None
        self.issues = []
        self.file_path = file_path

    def visit_FunctionDef(self, node):
        for arg in node.args.args:
            if not re.match(r'^_*[a-z][a-z0-9_]*$', arg.arg):
                self.issues.append((node.lineno, "S010", f"Argument name '{arg.arg}' should be snake_case"))

        defaults = node.args.defaults
        for default in defaults:
            if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                self.issues.append((node.lineno, "S012", "Default argument value is mutable"))
                break

        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(self.get_parent_function(node), ast.FunctionDef):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if not re.match(r'^_*[a-z][a-z0-9_]*$', target.id):
                        self.issues.append((node.lineno, "S011", 
                                         f"Variable '{target.id}' in function should be snake_case"))
        self.generic_visit(node)

    def get_parent_function(self, node):
        parent = self.get_parent(node)
        while parent and not isinstance(parent, ast.FunctionDef):
            parent = self.get_parent(parent)
        return parent

    def get_parent(self, node):
        for parent in ast.walk(self.tree):
            for child in ast.iter_child_nodes(parent):
                if child == node:
                    return parent
        return None

    def analyze(self, code):
        self.tree = ast.parse(code)
        self.visit(self.tree)
        return self.issues


class CodeAnalyzer:
    def __init__(self):
        self.issues = []

    @staticmethod
    def check_line_length(line):
        return len(line.rstrip('\n')) > 79

    @staticmethod
    def check_indentation(line):
        if line.strip() == '':
            return False
        indent = len(line) - len(line.lstrip())
        return indent % 4 != 0

    @staticmethod
    def check_semicolon(line):
        code_part = line.split('#')[0]
        return code_part.rstrip().endswith(';')

    @staticmethod
    def check_inline_comment_spacing(line):
        if '#' not in line:
            return False
        code_before_comment = line.split('#')[0]
        if code_before_comment.strip() == '':
            return False
        return not code_before_comment.endswith('  ')

    @staticmethod
    def check_todo(line):
        if '#' not in line:
            return False
        comment_part = line.split('#')[1].lower()
        return 'todo' in comment_part

    @staticmethod
    def check_construction_spaces(line):
        match = re.match(r'^(\s*)(class|def)(\s+)(\w+)', line)
        if match and len(match.group(3)) > 1:
            return True, match.group(2)
        return False, None

    @staticmethod
    def check_class_name(line):
        match = re.match(r'^(\s*)class(\s+)(\w+)', line)
        if match:
            class_name = match.group(3)
            if not re.match(r'^[A-Z][a-zA-Z0-9]*$', class_name):
                return True, class_name
        return False, None

    @staticmethod
    def check_function_name(line):
        match = re.match(r'^(\s*)def(\s+)(\w+)', line)
        if match:
            func_name = match.group(3)
            name_without_underscores = func_name.strip('_')
            if not re.match(r'^[a-z][a-z0-9_]*$', name_without_underscores):
                return True, func_name
        return False, None

    def analyze_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                lines = content.splitlines()
                
                ast_analyzer = ASTAnalyzer(file_path)
                ast_issues = ast_analyzer.analyze(content)
                for line_no, code, message in ast_issues:
                    self.issues.append((file_path, line_no, code, message))

                blank_lines_count = 0
                for line_number, line in enumerate(lines, 1):
                    issues = []
                    
                    if self.check_line_length(line):
                        issues.append(("S001", "Too long"))
                    
                    if self.check_indentation(line):
                        issues.append(("S002", "Indentation is not a multiple of four"))
                    
                    if self.check_semicolon(line):
                        issues.append(("S003", "Unnecessary semicolon"))
                    
                    if self.check_inline_comment_spacing(line):
                        issues.append(("S004", "At least two spaces required before inline comments"))
                    
                    if self.check_todo(line):
                        issues.append(("S005", "TODO found"))
                    
                    if line.strip() == '':
                        blank_lines_count += 1
                    else:
                        if blank_lines_count > 2:
                            issues.append(("S006", "More than two blank lines used before this line"))
                        blank_lines_count = 0
                    
                    has_extra_spaces, construct = self.check_construction_spaces(line)
                    if has_extra_spaces:
                        issues.append(("S007", f"Too many spaces after '{construct}'"))
                    
                    is_bad_class, class_name = self.check_class_name(line)
                    if is_bad_class:
                        issues.append(("S008", f"Class name '{class_name}' should use CamelCase"))
                    
                    is_bad_func, func_name = self.check_function_name(line)
                    if is_bad_func:
                        issues.append(("S009", f"Function name '{func_name}' should use snake_case"))
                    
                    for code, message in issues:
                        self.issues.append((file_path, line_number, code, message))
                        
        except Exception as e:
            print(f"Error analyzing {file_path}: {str(e)}")

    def process_path(self, path):
        if os.path.isfile(path):
            if path.endswith('.py'):
                self.analyze_file(path)
        else:
            for root, _, files in os.walk(path):
                for file in sorted(files):
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        self.analyze_file(file_path)

    def print_issues(self):
        sorted_issues = sorted(self.issues, key=lambda x: (x[0], x[1], x[2]))
        for file_path, line_number, code, message in sorted_issues:
            print(f"{file_path}: Line {line_number}: {code} {message}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python code_analyzer.py <directory-or-file>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist")
        sys.exit(1)

    analyzer = CodeAnalyzer()
    analyzer.process_path(path)
    analyzer.print_issues()


if __name__ == "__main__":
    main()
