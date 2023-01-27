Approach :- 
-> We have used a DFS based approach to solve this problem.
-> As the problem states that if a ‘O’ is to be considered in a surrounded region it should be in a region which is surrounded by 	‘X’s on all four sides. 
-> Therefore we can traverse through all the ‘O’s present on the boundaries of the board and mark all the reachable ‘O’s from 	them in 4 directions.
-> In our solution we have marked these reachable ‘O’s by replacing them with ‘@’s.
-> After the replacing/changing is done we replace the remaining ‘O’s with ‘X’s and the changed ‘@’s back to ‘O’s.

change function :-
-> This function is responsible for the replacement of ‘O’s that are reachable by boundary ‘O’s to ‘@’s.
-> It uses depth first search algorithm to search for all the possible paths in 4 neighbouring blocks of the current block.
-> It checks whether the current block is visited or not and then marks it as visited if not previously.
-> Takes board matrix, visited matrix, current row, current column, total rows and total columns as parameters.