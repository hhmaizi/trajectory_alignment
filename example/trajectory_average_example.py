from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
from matplotlib import pyplot as plt

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = 'raw_trajectories' , 
		pattern = '.data' ,
		comment_char = '%' , 
		dt = 0.1045 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '10/10/13' , 
		notes = 'one of my first experiments')

print( trajectory_list[ 0 ] )

#compute the average of all the trajectories in the list
best_average , worst_average = average_trajectories( trajectory_list , max_frame = 500 )

plt.figure()
plt.subplot(221)
plt.plot( best_average.coord()[ 0 ] , best_average.coord()[ 1 ] ,\
		'k-' , label = best_average.annotations( 'protein' ) + ' average trajectory')
plt.plot( best_average.coord()[ 0 ] , best_average.coord()[ 1 ] * 0 ,\
		'r--' , label = 'invagination axis')
plt.xlabel( 'Inward movement (' + best_average.annotations( 'coord_unit' ) + ')' )
plt.ylabel( best_average.annotations( 'coord_unit' ) )
plt.legend( loc = 'best' )

plt.subplot(222)
plt.plot( best_average.t() , best_average.coord()[ 0 ] ,\
		'k-' , label = best_average.annotations( 'protein' ) + ' inward movement')
plt.plot( best_average.t() , best_average.coord()[ 0 ] + best_average.coord_err()[ 0 ],\
		'--' , color = '0.75' , label = 'Std. of the aligned\ntrajectories')
plt.plot( best_average.t() , best_average.coord()[ 0 ] - best_average.coord_err()[ 0 ],\
		'--' , color = '0.75' )
plt.xlabel( 'Time (' + best_average.annotations( 't_unit' ) + ')' )
plt.ylabel( 'Inward movement (' + best_average.annotations( 'coord_unit' ) + ')' )
plt.legend( loc = 'best' )

plt.subplot(224)
plt.plot( best_average.t() , best_average.f() , 'k-' ,\
		label = best_average.annotations( 'protein' ) + ' normalized\nfluorescence intensity')
plt.plot( best_average.t() , best_average.f() + best_average.f_err(),\
		'--' , color = '0.75' , label = 'Std. of the fluorescence intensity')
plt.plot( best_average.t() , best_average.f() - best_average.f_err(),\
		'--' , color = '0.75' )
plt.xlabel( 'Time (' + best_average.annotations( 't_unit' ) + ')' )
plt.legend( loc = 'best' )

plt.show()
