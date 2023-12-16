# things needed:
    # gui to spawn tomogatchi and interact with it
    # canvas to have visual of tomogatchi and changes with mood
    # counter either on timer or based on actions performed to tick down hunger
        # also need like happines or cleanliness meter? could maybe just do in text
    # other interactables
        # feed and play button
# other requirements
    # three functions at least
        # easily done with buttons
    # external modual besides tkinter
        # need random anyway
    # file input or output
    # list or dictionary
    # graphics

dead = False

from tkinter import *
import random

pet = {'name': '', 'type': '', 'age': 0, 'hunger': 0, 'happiness': 0, 'toys': [], 'pic': ''}

petToys = {'dog': ['frisbee', 'bone'], 'baby': ['stuffed bear', 'real bear'], 'monkey': ['monkey money', 'banan']}
    
petoptions = list(petToys.keys())

def birth():
    
    guy = n.get()
    ptype = t.get()

    if (ptype in petoptions) and (guy != ''):
        pet['type'] = ptype
        pet['name'] = guy
        pet['toys'] = list('')
        pet['hunger'] = 0
        pet['age'] = 0
        
        if 'dog' in pet['type']:
            canvas.delete("all")
            canvas.create_image(250,250, anchor=CENTER, image=dog)
        
        if 'baby' in pet['type']:
            canvas.delete("all")
            canvas.create_image(250,250, anchor=CENTER, image=baby)
        
        if 'monkey' in pet['type']:
            canvas.delete("all")
            canvas.create_image(250,250, anchor=CENTER, image=monkey)
        
        
        print('valid pet type')
        print(pet['type'])
        
    else:
        print('please enter a valid pet type')
        for option in petoptions:
            print(option)
        print('or please enter a name for your pet')
        

def stats():
    print('-------------------------------------')
    print(pet['type'] + ' ' + pet['name'] + ' is doing great')
    print('the toys your pet currently has are: ' + str(len(pet['toys'])))
    for toy in pet['toys']:
        print(toy)
    print('your pet is currently at hunger: ' + str(pet['hunger']) + '/100')
    print('your pet is ' + str(pet['age']) + ' tamadays old.')
    
def death():
    if pet['type'] == '':
        print('please begin the game first')
    else:
        guy = n.get()
        ptype = t.get()
        with open(pet['name'] + "'s death certificate", 'w') as c:
            c.write('your ' + str(pet['type']) + ', ' + str(pet['name']) + ' lived to be ' + str(pet['age']) + ' tamadays old.\n')
            c.write('they had ' + str(len(pet['toys'])) + ' toys and passed peacefully')
        pet['type'] = ''
        pet['name'] = ''
        pet['toys'] = list('')
        pet['hunger'] = 0
        pet['age'] = 0
        canvas.delete("all")
        canvas.create_image(250,250, anchor=CENTER, image=egg)
    
def killed():
    if pet['type'] == '':
        print('please begin the game first')
    else:
        guy = n.get()
        ptype = t.get()
        with open(pet['name'] + "'s death certificate", 'w') as c:
            c.write('your ' + str(pet['type']) + ', ' + str(pet['name']) + ' lived to be ' + str(pet['age']) + ' tamadays old.\n')
            c.write('they had ' + str(len(pet['toys'])) + ' toys and murdered brutally')
        pet['type'] = ''
        pet['name'] = ''
        pet['toys'] = list('')
        pet['hunger'] = 0
        pet['age'] = 0
        canvas.delete("all")
        eggtype = random.choice(eggtypes)
        canvas.create_image(250,250, anchor=CENTER, image=eggtype)

def feed():

    if pet['type'] == '':
        print('please begin the game first')
    else:
        
        newhunger = pet['hunger'] - 20
        if newhunger < 0:
            newhunger = 0
        
        pet['hunger'] = newhunger
        pet['hunger'] += 10
        pet['age'] += 1
        print('-------------------------------------')
        print('fed your pet')
        if pet['hunger'] > 100:
            death()
        stats()
        
def play():
    
    if pet['type'] == '':
        print('please begin the game first')
    else:
        print('-------------------------------------')
        print(pet['name'] + ' had fun playing')
        pet['hunger'] += 10
        pet['age'] += 1
        stats()
        if pet['hunger'] > 100:
            death()
    
def gnt():
    
    if pet['type'] == '':
        print('please begin the game first')
    else:
        print('-------------------------------------')
        print('select a new toy for your pet')
        toyoptions = petToys[pet['type']]
        print(toyoptions)
        
        toyname = gt.get()
        
        if (toyname not in petToys[pet['type']]) and (toyname not in list(pet['toys'])):
            print('please enter a valid toy name')
        else:
            print('valid toy')
            pet['toys'].append(toyname)
            print('-------------------------------------')
            print('you selected ' + toyname + ' for ' + pet['name'])
            print (pet['toys'])
            pet['hunger'] += 10
            pet['age'] += 1
            stats()
            if pet['hunger'] > 100:
                death()
            

root = Tk()
root.title('tamagotchi')

egg = PhotoImage(file="egg.png")
egg1 = PhotoImage(file='egg1.png')
egg2 = PhotoImage(file='egg2.png')

eggtypes = [egg, egg1, egg2]

eggtype = random.choice(eggtypes)

canvas = Canvas(root, width=500, height=500)
canvas.grid(row=0, column=0)

canvas.create_image(250,250, anchor=CENTER, image=eggtype)

dog = PhotoImage(file='dog.png')
baby = PhotoImage(file='baby.png')
monkey = PhotoImage(file='monkey.png')

species = Label(root, text='what kind of pet would you like? options: dog, baby, monkey')
species.grid(row=1, column=0)

t = Entry(root)
t.grid(row=1, column=1)

lname = Label(root, text='name your buddy:')
lname.grid(row=2, column=0)

n = Entry(root)
n.grid(row=2, column=1)

adopt = Button(root, text='adopt tamagotchi', command=birth)
adopt.grid(row=3, column=1)

kill = Button(root, text='kill tamagotchi', command=killed)
kill.grid(row=3, column=2)

f = Button(root, text='feed', command=feed)
f.grid(row=4, column=0)

p = Button(root, text='play', command=play)
p.grid(row=4, column=1)

toyname = Label(root, text='enter the name of the toy you want:')
toyname.grid(row=5, column=0)

getToy = Button(root, text='get new toy', command=gnt)
getToy.grid(row=5, column=2)

gt = Entry(root)
gt.grid(row=5, column=1)