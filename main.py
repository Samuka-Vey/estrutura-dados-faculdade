from array_nao_ordenado import UnsortedArray as unsorted
if __name__ == "__main__":
    def dobro(x):
        print(x * 2)
    array = unsorted(10)
    array.insert(1)
    array.insert(2)
    array.insert(3)
    array.insert(4)
    array.insert(5)
    array.traverse(print)
    
    print(f"O elemento 3 está no índice: {array.find(3)}")
    array.delete(2)
    array.traverse(print)
    
    # dobro da lista
    array.traverse(dobro)
    array.traverse(print)    