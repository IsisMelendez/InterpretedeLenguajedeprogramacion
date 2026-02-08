class Interpreter:
    def __init__(self):
        self.symbol_table = {}
    
    def interpret(self, ast):
        if ast:
            for node in ast:
                self._execute(node)
    
    def _execute(self, node):
        if node is None: return
        node_type = node[0]
        
        if node_type == 'assign':
            _, var_name, expr = node
            self.symbol_table[var_name] = self._evaluate(expr)
        elif node_type == 'print':
            print(self._evaluate(node[1]))
        elif node_type == 'if':
            _, cond, t_block, f_block = node
            if self._evaluate(cond):
                for s in t_block: self._execute(s)
            else:
                for s in f_block: self._execute(s)
        elif node_type == 'while':
            _, cond, block = node
            while self._evaluate(cond):
                for s in block: self._execute(s)

    def _evaluate(self, node):
        if node is None: return None
        if not isinstance(node, tuple): return node
        
        node_type = node[0]
        
        if node_type in ['number', 'string', 'bool']:
            return node[1]
            
        elif node_type == 'id':
            var_name = node[1]
            if var_name in self.symbol_table:
                return self.symbol_table[var_name]
            print(f"Error: variable '{var_name}' no definida")
            return None 
            
        elif node_type == 'binop':
            _, op, left, right = node
            l = self._evaluate(left)
            r = self._evaluate(right)
            
            
            if l is None or r is None:
                return None
                
            if op == '+': return l + r
            if op == '-': return l - r
            if op == '*': return l * r
            if op == '/': return l / r if r != 0 else 0
            if op == '<': return l < r
            if op == '>': return l > r
            if op == '==': return l == r
            if op == '!=': return l != r
            if op == 'AND': return l and r
            if op == 'OR': return l or r
            
        elif node_type == 'not':
            val = self._evaluate(node[1])
            return not val if val is not None else None
        
        return None

def interpret_code(code, interpreter=None):
    from parser import parse 
    if interpreter is None:
        interpreter = Interpreter()
    ast = parse(code)
    interpreter.interpret(ast)
    return interpreter