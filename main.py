import sys
from interpreter import interpret_code, Interpreter

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
        return None

def repl():
    """Modo interactivo REPL"""
    print("Interprete de mini lenguaje")
    print("Palabras reservadas: cuando, deotro, durante, decir")
    print("Escribe 'salir' para terminar\n")
    
    interpreter = Interpreter()
    
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() == 'salir':
                break
            if line.strip():
                interpret_code(line, interpreter)
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        code = read_file(filename)
        
        if code:
            interpret_code(code)
    else:
        
        repl()

if __name__ == '__main__':
    main()