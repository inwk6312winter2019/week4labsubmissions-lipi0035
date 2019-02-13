#Task 1
import math
class Point():
  def __init__(self,x = 0.0, y = 0.0):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "(%.2f,%.2f)" %(self.x,self.y)
	
  def distance_between_points(self,p):
    x = math.pow(self.x-p.x,2)
    y = math.pow(self.y-p.y,2)
    return (math.sqrt(x+y))
    
point1 = Point(3,8)
point2 = Point(11,5)
p = Point()
print("Distance between two points {0} and {1} is : {2:.2f}" .format(point1,point2,point1.distance_between_points(point2)))

#Task 2
#Task 2-a
class Rectangle(Point):
  def __init__(self,width = 0.0,height = 0.0,corner = Point(0.0,0.0)):
    self.width = width
    self.height = height
    self.corner = corner
    
def find_centre(Rectangle):
  centre_y = Rectangle.height/2
  centre_x = Rectangle.width/2
  return (centre_x,centre_y)
 
p = Point()
rect = Rectangle(10,20,p)
centre = find_centre(rect)
print("Coordinates of centre of a rectangle with one corner at (0,0) is : "+str(centre))

#Task 2-b
def move_rectangle(Rectangle,dx,dy):
  Rectangle.corner.x = Rectangle.corner.x + dx
  Rectangle.corner.y = Rectangle.corner.y + dy
  return ((Rectangle.corner.x,Rectangle.corner.y))

cor = Point(4,5)
dx = 2
dy = 2
mv_rect = Rectangle(corner = cor)
moved_corner = move_rectangle(mv_rect,dx,dy)
print("Coordinates of corner of new rectangle : " +str(moved_corner))

#Task 2-c 
def move_rectangle_new(rect,dx,dy):
  #c = Point()
  r = Rectangle(rect.corner.x,rect.corner.y)
  r.corner.x = rect.corner.x + dx
  r.corner.y = rect.corner.y + dy
  return r
  
cor_new = Point(4,5)
dx = 3
dy = 4
mv_rect_new = Rectangle(corner = cor_new)
moved_corner_new = move_rectangle_new(mv_rect_new,dx,dy)
print("Coordinates of corner of new rectangle with another rectangle object : (%d,%d)" %(moved_corner_new.corner.x,moved_corner_new.corner.y))

#Task 3

class Time:
  def __init__(self, hour = 00, minute = 00, second = 00):
    self.hour = hour
    self.minute = minute
    self.second = second
	
def print_time(time):
    print("%.2d:%.2d:%.2d"%(time.hour,time.minute,time.second))
	
t = Time(9,10,12)
print_time(t)

#Task 4
import datetime
def is_after(t1,t2):
  t1 = datetime.timedelta(hours = t1.hour, minutes = t1.minute, seconds = t1.second)
  t2 = datetime.timedelta(hours = t2.hour, minutes = t2.minute, seconds = t2.second)
  return t1>t2
  
t1 = Time(6,5,20)
t2 = Time(4,6,10)
print("Does t1 follows t2 chronologically? : %r" %(is_after(t1,t2)))

#Task 5 - 6
class Point():
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
    
  def __str__(self):
    return str((self.x,self.y))
	
  def __add__(self,other):
    pt = Point()
    if isinstance(other,Point):
      pt.x = pt.x + self.x + other.x
      pt.y = pt.y + self.y + other.y
	  #return pt
    elif isinstance(other,tuple):
      pt.x = pt.x + self.x + other[0]
      pt.y = pt.y + self.y + other[1]
    return pt  
  
  def __radd__(self,other):
    return self.__add__(other)
	
pt1 = Point(3,4)
pt2 = (4,5)
pt3 = pt1 + pt2
pt4 = pt2 + pt1
print(pt3+pt4)
print(pt3)

#Task 7
class Kangaroo:
  def __init__(self,pouch_contents = []):
    self.pouch_contents = pouch_contents
	
  def put_in_pouch(self,obj):
    if isinstance(obj,Kangaroo):
      for elem in obj.pouch_contents:
        self.pouch_contents.append(elem)
    else:
      self.pouch_contents.append(obj)
	  
  def __str__(self):
    return (str(self.pouch_contents))

kanga = Kangaroo([1,2,3])
roo = Kangaroo([4,5,6])
e = "lipi"
kanga.put_in_pouch(roo)
kanga.put_in_pouch(e)
print(kanga)

#Task 8 Same as Task 6

#Task 9
class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
	
for cl1 in [Vehicle, LandVehicle, TrackedVehicle]:
	for cl2 in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(cl1,cl2),end='\t')
	print()
print()
#Task 10
class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass

vehicle = Vehicle()
landvehicle = LandVehicle()
trackedvehicle = TrackedVehicle()

for ob in [vehicle, landvehicle, trackedvehicle]:
	for cl in [Vehicle, LandVehicle, TrackedVehicle]:
		print(isinstance(ob,cl),end='\t')
	print()

#Task 11
class IPv4Address:
  def __init__(self,network = [],mask = 32):
    self.network = network
    subnet = []
    x,y = 0,0
    m,n = divmod(mask,8)
    for i in range(m):
      subnet.append(255)
    for j in range(n):
      x = x+(1*(2**y))
      y = y+1
    subnet.append(x)
    if(len(subnet)<4):
      subnet.append(0)
    self.mask = subnet
	
	
  def getNetwork(self):
    return self.network
	
  def getMask(self):
    return self.mask
	
  def getAddress(self):
    return [self.network,self.mask]
	
ipv4 = IPv4Address([10,0,1,7],25)
net = ipv4.getNetwork()
mask = ipv4.getMask()
addr = ipv4.getAddress()
print(net)
print(mask)
print(addr)

#Task 12
import random
import sys

def subnet_calc():
    try:
        print("\n")

        #Checking IP address validity
        while True:
            ip_address = input("Enter an IP address: ")

            #Checking octets            
            a = ip_address.split('.')

            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        #Checking Subnet Mask validity
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            #Checking octets            
            b = subnet_mask.split('.')

            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break

            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue

	############# Application #1 - Part #2 #############

        #Algorithm for subnet identification, based on IP and Subnet Mask

        #Convert mask to binary string
        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".")
        #print mask_octets_decimal

        for octet_index in range(0, len(mask_octets_decimal)):

            #print bin(int(mask_octets_decimal[octet_index]))

            binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]
            #print binary_octet

            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)

            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)

        #print mask_octets_padded

        decimal_mask = "".join(mask_octets_padded)
        #print decimal_mask   #Example: for 255.255.255.0 => 11111111111111111111111100000000

        #Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return positive value for mask /32

        #print no_of_zeros
        #print no_of_ones
        #print no_of_hosts

        #Obtaining wildcard mask
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))

        #print wildcard_octets

        wildcard_mask = ".".join(wildcard_octets)
        #print wildcard_mask

    ############# Application #1 - Part #3 #############

        #Convert IP to binary string
        ip_octets_padded = []
        ip_octets_decimal = ip_address.split(".")

        for octet_index in range(0, len(ip_octets_decimal)):

            binary_octet = bin(int(ip_octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)

            else:
                ip_octets_padded.append(binary_octet)

        #print ip_octets_padded

        binary_ip = "".join(ip_octets_padded)

        #print binary_ip   #Example: for 192.168.2.100 => 11000000101010000000001001100100

        #Obtain the network address and broadcast address from the binary strings obtained above

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        #print network_address_binary

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        #print broadcast_address_binary

        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)

        #print net_ip_octets

        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        #print net_ip_address

        network_address = ".".join(net_ip_address)
        #print network_address

        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet+8]
            bst_ip_octets.append(bst_ip_octet)

        #print bst_ip_octets

        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        #print bst_ip_address

        broadcast_address = ".".join(bst_ip_address)
        #print broadcast_address

        #Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

        ############# Application #1 - Part #4 #############

        #Generation of random IP in subnet
        while True:
            generate = input("Generate random ip address from subnet? (y/n)")

            if generate == "y":
                generated_ip = []

                #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(bst_ip_address):
                    #print indexb, oct_bst
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print indexn, oct_net
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                #Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                #IP address generated from the subnet pool
                #print generated_ip
                y_iaddr = ".".join(generated_ip)
                #print(y_iaddr)

                print("Random IP address is: %s" % y_iaddr)
                print("\n")
                continue

            else:
                print("Exiting !\n")
                break

    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

subnet_calc()
