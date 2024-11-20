# Used for 'simulating' user-data collection during the development phase.

goals = ['Strength', 'Size', 'Cardio']

targets = ['Chest(Pectorals)', 'Back(Latissimus Dorsi)', 'Back(Traps)', 'Back(Spinal Erectors)',
           'Biceps', 'Triceps', 'Shoulders(Deltoid)', 'Abdominal', 'Legs(Hamstrings)', 'Legs(Quadriceps)', 'Legs(Glutes)']

equipment = ['Bodyweight', 'Resistance band', 'Dumbbells', 'Machines', 'Kettlebell', 'Barbell']

level = ['Beginner', 'Intermediate', 'Advanced']


def collect():
    
    userGoals = []
    userTargets = []
    userEquipment = []
    userLevel = []
    inputsCollected = 4
    
    while inputsCollected != 0:
        
        print('Strength, Size, Cardio')
        goalsIn = input('Enter your current fitness goal: ')
        inputsCollected -=1
        print('Chest, Back, Biceps, Triceps, Shoulders, Abdominal, Legs')
        targetsIn = input('Enter the areas you would like to target: ')
        inputsCollected -=1
        print('Bodyweight, Resistance band, Dumbbells, Machines, Kettlebell, Barbell')
        equipmentIn = input('Enter your current equipment: ')
        inputsCollected -=1
        print('Beginner, Intermediate, Advanced')
        levelIn = input('Enter your current level: ')
        inputsCollected -=1
        
    print('~ ~ All data collected ~ ~') 

    
collect()
        
    
    