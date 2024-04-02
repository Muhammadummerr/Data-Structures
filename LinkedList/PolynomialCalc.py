from Singly_linklist import SinglyLinkedList

class Nodes():
    def __init__(self,coeff,polynomial):
        self.coeff = coeff
        self.polynomial=polynomial
        self.next=None
class PolynomialLinklist(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    @staticmethod
    def displayPolynomial(polynomial):
        head = polynomial.head
        ans = ''
        while head!=None and head.polynomial !=0:
            ans+=f"{head.coeff}X^{head.polynomial} + "
            head = head.next
        ans+=f"{head.coeff}X^{head.polynomial}"
        return ans
    def append(self, newnode):
        head = self.head
        flag = False
        while head!=None:
            if head.polynomial == newnode.polynomial:
                head.coeff+=newnode.coeff
                flag=True
                break
            head=head.next
        if flag==False:
            super().append(newnode)
        return

class PolynomialCalc(SinglyLinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.Menu()
    def Menu(self):
        print(f"""Welcome to Polynomial Calculator\n
              This calculator is command line based calculator to ADD,SUBTRACT and MULTIPLY POLYNOMIALS.
              """)
        while True:
            command = input("Press any key to proceed to Calculator\nPress 0 to exit\n")
            if command=='0':
                break
            poly1 = self.GetPolynomial()
            poly2 = self.GetPolynomial()
            command = input("""Press the following keys to peroform respective tasks\n
                            Press 1 to ADD\n
                            Press 2 to Subtract\n
                            Press 3 to Multiply""")
            if command=="1":
                result = self.Addpolynomials(poly1,poly2)
                # print(result,poly1)
                print("Polynomial 1 :",PolynomialLinklist.displayPolynomial(poly1))
                print("Polynomial 2 :",PolynomialLinklist.displayPolynomial(poly2))
                print("Resultant:",PolynomialLinklist.displayPolynomial(result))
            elif command=="2":
                result = self.Subpolynomials(poly1,poly2)
                print("Polynomial 1 :",PolynomialLinklist.displayPolynomial(poly1))
                print("Polynomial 2 :",PolynomialLinklist.displayPolynomial(poly2))
                print("Resultant:",PolynomialLinklist.displayPolynomial(result))
            elif command=="3":
                result = self.MulPolynomials(poly1,poly2)
                print("Polynomial 1 :",PolynomialLinklist.displayPolynomial(poly1))
                print("Polynomial 2 :",PolynomialLinklist.displayPolynomial(poly2))
                print("Resultant:",PolynomialLinklist.displayPolynomial(result))
    def print(self):
        super.__init__()
        return
    def add(self,coeff,degree,obj):
        node = Nodes(int(coeff),degree)
        head = obj.append(node)
        return head
    def GetPolynomial(self):
        coeff_linklist = PolynomialLinklist()
        
        degreePoly  = int(input("Input Degree of polynomial:\n"))
        for degree in range(degreePoly,-1,-1):
            coeff = input(f"Enter coefficient of X**{degree}:")
            # self.head = PolynomialLinklist()
            self.add(coeff,degree,coeff_linklist)
        print(coeff_linklist.head.coeff,coeff_linklist.len())
        return coeff_linklist
    def Addpolynomials(self,p1,p2):
        h1 = p1.head
        h2 = p2.head
        result = PolynomialLinklist()
        while h1!=None and h2!=None:
            sum_ = h1.coeff+h2.coeff
            result.append(Nodes(sum_,h1.polynomial))
            h1=h1.next
            h2=h2.next
        return result
    def Subpolynomials(self,p1,p2):
        h1 = p1.head
        h2 = p2.head
        result = PolynomialLinklist()
        while h1!=None and h2!=None:
            sub_ = h1.coeff-h2.coeff
            result.append(Nodes(sub_,h1.polynomial))
            h1=h1.next
            h2=h2.next
        return result
    def MulPolynomials(self,p1,p2):
        h1 = p1.head
        result = PolynomialLinklist()
        while h1!=None:
            print(h1.coeff)
            h2 = p2.head
            while h2!=None:
                node = Nodes(h1.coeff*h2.coeff,h1.polynomial+h2.polynomial)
                result.append(node)
                h2=h2.next
            h1= h1.next
        # self.displayPolynomial(result)
        return result
Calc = PolynomialCalc()
