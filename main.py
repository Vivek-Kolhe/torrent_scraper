import pprint
import pyperclip
import yify
import torrent1337x
import zooqle

print("Choose torrent search engine:\n1. Yify\n2. 1337x\n3. Zooqle")
choice = int(input("Enter choice: "))
query = input("Search something? ").lower()
flag = True

if choice == 1:
    query = query.replace(" ", "-")
    x = yify.yify(query)
elif choice == 2:
    query = query.replace(" ", "%20")
    x = torrent1337x.torrent1337x(query)
elif choice == 3:
    query = query.replace(" ", "+")
    x = zooqle.zooqle(query)
else:
    flag = False
    print("Invalid choice. Exiting..")

if flag:
    pprint.pprint(x)
    try:
        ind = int(input("Enter index of the magnet to copy: "))
        pyperclip.copy(x[ind-1]["Magnet"])
        print("Magnet Copied to your clipboard!")
    except Exception:
        print("Enter valid index!")