# Used for 'simulating' user-data collection during the development phase.

goals = ['Strength', 'Size', 'Cardio']

targets = ['Chest(Pectorals)', 'Back(Latissimus Dorsi)', 'Back(Traps)', 'Back(Spinal Erectors)',
           'Biceps', 'Triceps', 'Shoulders(Deltoid)', 'Abdominal', 'Legs(Hamstrings)', 'Legs(Quadriceps)', 'Legs(Glutes)']

equipment = ['Bodyweight', 'Resistance band', 'Dumbbells', 'Machines', 'Kettlebell', 'Barbell']

level = ['Beginner', 'Intermediate', 'Advanced']

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
        
        print('Strength, Size, Cardio')
        goalsIn = input('Enter your current fitness goal: ').strip().lower()
        stsv(goalsIn, 'goal', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print('Chest, Back, Biceps, Triceps, Shoulders, Abdominal, Legs')
        targetsIn = input('Enter the areas you would like to target: ').strip().lower()
        stsv(targetsIn, 'target', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print('Bodyweight, Resistance band, Dumbbells, Machines, Kettlebell, Barbell')
        equipmentIn = input('Enter your current equipment: ').strip().lower()
        stsv(equipmentIn, 'equipment', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        print('Beginner, Intermediate, Advanced')
        levelIn = input('Enter your current level: ').strip().lower()
        stsv(levelIn, 'level', userGoals, userTargets, userEquipment, userLevel)
        inputsCollected -=1
        
    print('~ ~ All data collected ~ ~') 

    
collect()
        
        
        
            
            


    
    
    