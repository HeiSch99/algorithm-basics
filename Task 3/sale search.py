import xml.etree.ElementTree as ET
from heapq import nlargest

# ---------- Function for parsing an XML file ---------- #

def parse_data(xml_file):
    """Parse an XML file and return list of (product, price) records."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    sales = []
    for sale in root.findall('sale'):
        product = sale.get('product')
        price = float(sale.get('price'))
        sales.append((product, price))
    return sales

# ---------- Data implementation as a linked list ---------- #

class Node:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, product, price):
        """Insert new sales record at the beginning."""
        new_node = Node(product, price)
        new_node.next = self.head
        self.head = new_node

    def search (self, product):
        """Search for a product and return its total sales."""
        total = 0
        current = self.head
        
        while current:
            if current.product == product:
                total += current.price
            current = current.next

        return total if total > 0 else None

    def all_sales(self):
        """Return dictionary of total sales per product."""
        current = self.head
        totals = {}

        while current:
            totals[current.product] = totals.get(current.product, 0) + current.price
            current = current.next
        
        return totals

# ---------- Data implementation as a hash table ---------- #

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, product, price):
        """Inserts or updates total sales per product."""
        self.table[product] = self.table.get(product, 0) + price

    def search(self, product):
        """Returns total sales for a product."""
        return self.table.get(product, None)
    
    def all_sales(self):
        """Returns dictionary of all product sales."""
        return self.table

# ---------- Function for sorting query in descending order ---------- #

def sort_sales(sales_dict, descending = True):
    """Return all products sorted by total sales."""
    return sorted(sales_dict.items(), key = lambda x: x[1], reverse = descending)

# ---------- Usage ---------- #
if __name__ == "__main__":
    # XML file example
    xml_file = "./Task 3/sales.xml"

    # Parses XML data
    sales = parse_data(xml_file)

    # Asks user which data structure to use
    print("Choose a data structure for storing sales data:")
    print("1. Linked List")
    print("2. Hash Table")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        ds = LinkedList()
        mode = "Linked List"
    elif choice == "2":
        ds = HashTable()
        mode = "Hash Table"
    else:
        print("Invalid choice, using Hash Table by default")
        ds = HashTable()
        mode = "Hash Table"

    print(f"\nUsing: {mode}")

    # Insert all sales
    for product, price in sales:
            ds.insert(product, price)

    # Query 1: Search by product name
    print("\n[First  Query]: Search by product name")
    product_name = "Oranges"
    result = ds.search(product_name)
    if result is not None:
        print(f"Total sales for '{product_name}': ${result:.2f}")
    else:
        print(f"Product '{product_name}' not found.")

    # Query 2: Sort all products by total sales in descending order
    print("\n[Second Query]: Sort all products by its value in descending order")
    totals = ds.all_sales()
    sorted_sales = sort_sales(totals, descending = True)
    for product, total in sorted_sales:
        print(f"- {product}: ${total:.2f}")