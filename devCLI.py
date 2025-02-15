# Used for 'simulating' user-data collection during the development phase.

goals =  ['Strength' 'Plyometrics' 'Cardio' 'Stretching' 'Powerlifting' 'Strongman'
 'Olympic Weightlifting']

targets =  ['Abdominals' 'Adductors' 'Abductors' 'Biceps' 'Calves' 'Chest' 'Forearms'
 'Glutes' 'Hamstrings' 'Lats' 'Lower Back' 'Middle Back' 'Traps' 'Neck'
 'Quadriceps' 'Shoulders' 'Triceps']

equipment = ['Bands' 'Barbell' 'Kettlebells' 'Dumbbell' 'Other' 'Cable' 'Machine'
 'Body Only' 'Medicine Ball' 'Exercise Ball' 'Foam Roll'
 'E-Z Curl Bar']

level = ['Beginner', 'Intermediate', 'Expert']

# Function for ensuring all collected data is 'standard format' and stored in the relevant lists.
def stsv(userIn, category, userGoals, userTargets, userEquipment, userLevel):
        

        
        if category == 'goal':
            split = userIn.split()
            for i in split:
                if i in [g.lower() for g in goals]:
                    userGoals.append(i)
                    
        elif category == 'target':
            split = userIn.split()
            for i in split:
                if i in [t.lower() for t in targets]:
                    userTargets.append(i)
        
        elif category == 'equipment':
            split = userIn.split()
            for i in split:
                if i in[e.lower() for e in equipment]:
                    userEquipment.append(i)
        
        elif category == 'level':
            split = userIn.split()
            for i in split:
                if i in[l.lower() for l in level]:
                    userLevel.append(i)

def collect():
    
    userGoals = []
    userTargets = []
    userEquipment = []
    userLevel = []
    inputsCollected = 4
    
    while inputsCollected != 0:
        
        print(goals)
        goalsIn = input('Enter your current fitness goal: ').strip().lower()
        stsv(goalsIn, 'goal', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print(targets)
        targetsIn = input('Enter the areas you would like to target: ').strip().lower()
        stsv(targetsIn, 'target', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print(equipment)
        equipmentIn = input('Enter your current equipment: ').strip().lower()
        stsv(equipmentIn, 'equipment', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print(level)
        levelIn = input('Enter your current level: ').strip().lower()
        stsv(levelIn, 'level', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        
    print('~ ~ All data collected ~ ~') 
    
    print(userGoals, userTargets, userEquipment, userLevel) 
        
        
        
            
            


    
    
collect()