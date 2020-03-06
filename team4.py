team_name = 'MoMo'
strategy_name = 'u b kind we b kind'
strategy_description = 'if they collude we also collude but if they betrayed  on last turn we betray'
import random    
def move(my_history, their_history, my_score, their_score):
    options = ['c', 'b']
    if len(my_history)==0:
        return random.choice(options)
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'  
    elif my_history[-1]=='b' and their_history[-1]=='c':
        return 'c' 
    elif my_history[-1]=='b' and their_history[-1]=='b':
        return 'b' 
    elif my_history[-1]=='c' and their_history[-1]=='c':
        return 'c' 
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='b',
              their_history='c', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
    if test_move(my_history='b',
              their_history='c', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
    if test_move(my_history='b',
              their_history='c', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='cbb',
              their_history='bbb', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')              