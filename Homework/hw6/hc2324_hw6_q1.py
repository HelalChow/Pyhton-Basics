def print_shifted_triangle(n, m, symbol):
    for i in range(n):
        print(m*" "+(n-i)*" "+(2*i+1)*symbol)

def print_pine_tree(n, symbol):
    for i in range(2,n+2):
        print_shifted_triangle(i,n-i+1, symbol)

def main():
    n = int(input("Please enter the number of triangles in the tree: "))
    symbol = input("Please enter the character filling the tree: ")
    print_pine_tree(n, symbol)
main()