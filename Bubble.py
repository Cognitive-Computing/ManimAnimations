from big_ol_pile_of_manim_imports import *
import numpy as np

class Bubble(Scene):
	def construct(self):
		array = self.get_array(10)
		values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
		value_group = self.put_values_in_array(array, values)
		title = TextMobject('Bubble Sort').scale(2).to_edge(UP)
		title_line = Line(title.get_right(), title.get_left()).scale(2).next_to(title, DOWN)
		self.play(Write(title), Write(title_line), runtime = 1.0)
		self.play(Write(array))
		self.wait()
		self.play(Write(VGroup(value_group)))
		self.show_bubble_simulation(array,values, value_group)
		self.wait(2)

	def get_array_box(self):
		box = Rectangle()
		box.set_width(0.7)
		box.set_height(0.5)
		return box

	def get_array(self, size):
		return VGroup([self.get_array_box() for i in range(size)]).arrange_submobjects(RIGHT, buff=0)

	def put_values_in_array(self,array, values):
		values_group = [TextMobject(str(element)).scale(0.5).move_to(array[i].get_center()) for element, i in zip(values, list(range(len(values))))]
		return values_group

	def swap_value(self, i,j, array, values_group):
		value_i_transform = values_group[i].copy().move_to(array[j].get_center())
		value_j_transform = values_group[j].copy().move_to(array[i].get_center())
		# self.wait()
		# self.play(Transform(values_group[i], value_i_transform), Transform(values_group[j], value_j_transform), run_time=0.3)
		self.play(Swap(values_group[i], values_group[j]), runtime=0.3)


	def show_bubble_simulation(self,array,values, values_group):
		for i in range(len(values)-1):
			for j in range(len(values)-i-1):
				# if i == 1 and j == 0:
				# 	self.wait(4.5)
				# 	self.play(Indicate(array[5]))
				# 	self.wait(7.5)
				# 	self.wait(13)
				# if i == 2 and j == 0:
				# 	self.wait(10)
				# 	self.play(Indicate(array[0]), Indicate(array[3]))
				# 	self.wait(2)
				# if i == 3 and j == 0:
				# 	self.wait(10)
				# 	self.play(Indicate(array[0]), Indicate(array[2]))
				# 	self.wait(2)

				# if i == 4 and j == 0:
				# 	self.wait(10)
				# 	self.play(Indicate(array[0]), Indicate(array[1]))
				# 	self.wait(2)

				# if i == 5 and j == 0:
				# 	self.wait(10)
				# 	self.play(Indicate(array[0]))
				# 	self.wait(2)

				self.wait(0.2)
				array[j].set_fill(BLUE, opacity=0.5)
				array[j+1].set_fill(BLUE, opacity=0.5)


				# if i == 0:
				# 	self.wait(6)
				# if i == 1:
				# 	self.wait(3.2)
				# if i == 2:
				# 	self.wait(4.2)
				# if i == 3:
				# 	self.wait(4.2)
				# if i == 4:
				# 	self.wait(4.2)
				# if i == 5:
				# 	self.wait(20)


				if values[j] > values[j+1]:
					array[j].set_fill(RED, opacity=0.5)
					array[j+1].set_fill(RED, opacity=0.5)

					temp = values[j]
					values[j] = values[j+1]
					values[j+1] = temp
					# self.wait(1)
					self.wait(0.1)
					self.swap_value(j,j+1,array,values_group)


					temp = values_group[j]
					values_group[j] = values_group[j+1]
					values_group[j+1] = temp

					array[j].set_fill(BLACK, opacity=0.1)
					array[j+1].set_fill(BLACK, opacity=0.1)
				else:
					array[j].set_fill(BLACK, opacity=0.1)
					array[j+1].set_fill(BLACK, opacity=0.1)
					self.wait(0.1)
		# self.wait(10)
				

class Introduction(Scene):
	def construct(self):
		text1 = TextMobject('BUBBLE SORT').scale(2).to_edge(UP)
		line1 = Line(text1.get_right(), text1.get_left(), buff=0).next_to(text1, DOWN)
		section1 = TextMobject('1. Bubble Sort Algorithm').scale(1).next_to(line1,DOWN).set_color(GREEN)
		section2 = TextMobject('2. Bubble Sort Simulation').scale(1).next_to(line1,DOWN).set_color(BLUE)
		section3 = TextMobject('3. Implementation In Python').scale(1).next_to(line1,DOWN).set_color(ORANGE)
		screen = ScreenRectangle().next_to(section1,DOWN).shift(DOWN*0.5)
		screen.set_width(10)
		screen.set_height(5)
		screen.set_stroke(color = YELLOW, width = 2)

		self.wait()
		self.play(Write(text1))
		self.play(GrowFromCenter(line1), run_time = 1.5)
		self.play(Write(screen), Write(section1))
		self.wait(4)
		self.play(ReplacementTransform(section1, section2))
		self.wait(4)
		self.play(ReplacementTransform(section2, section3))
		self.wait(2)
		
class Section1(Bubble, Scene):
	def construct(self):
		title = TextMobject('Algorithm').scale(2).to_edge(UP)
		title_line = Line(title.get_right(), title.get_left(), buff=0).next_to(title, DOWN)

		array1 = self.get_array(6).next_to(title_line, DOWN * 6)
		values1 = np.random.randint(10,90,6)
		value_group1 = self.put_values_in_array(array1, values1)

		array2 = self.get_array(6).next_to(title_line, DOWN * 6).to_edge(RIGHT)
		values2 = np.random.randint(10,90,6)
		value_group2 = self.put_values_in_array(array2, values2)

		self.wait()
		self.play(Write(title))
		self.play(GrowFromCenter(title_line))
		# self.play(Write(array1))
		# self.play(Write(VGroup(value_group1)))
		# self.show_bubble_simulation(array1,values1, value_group1)
		# self.wait(2)
		# self.play(FadeOut(VGroup(array1)), FadeOut(VGroup(value_group1)))
		self.DrawPartitionLine(title_line)
		self.wait(3)
		# self.write_algo()
		algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop = self.write_algo()
		# self.wait()
		self.play(Write(array2))
		self.play(Write(VGroup(value_group2)))
		self.wait(9.5)
		self.play(Indicate(array2[0]), Indicate(array2[5]))
		self.wait(5)
		self.show_bubble_simulation(array2,values2, value_group2)
		self.wait(2)
		self.play(FadeOut(VGroup(array2)), FadeOut(VGroup(value_group2)))

		## Time Complexity analysis ##

		self.wait(2)
		self.show_time_complexity(algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop)
		self.wait(2)


	def DrawPartitionLine(self, title_line):
		partition_line = Line(title_line.get_center(), DOWN*3)
		self.play(GrowFromCenter(partition_line))

	def write_algo(self):
		step1 =  TexMobject("Loop\\ for\\ i=0\\ to\\ i=N-1",tex_to_color_map={"for":GREEN, "i=0":YELLOW,"i=N-1":RED}).scale(0.8).to_edge(LEFT)
		step1.shift(UP*1.5)
		step2 =  TexMobject("Loop\\ for\\ j=0\\ to\\ j=N-i-1", tex_to_color_map={"for":GREEN, "j=0":YELLOW,"j=N-i-1":RED}).scale(0.8)
		step2.next_to(step1, DOWN).shift(RIGHT*0.5)
		step3 = TexMobject("if\\ arr[j]\\ >\\ arr[j+1]:", tex_to_color_map={"if":GREEN, "arr[j]\\ >\\ arr[j+1]": BLUE}).scale(0.8)
		step3.next_to(step2, DOWN).shift(RIGHT*0.5)
		swap = TexMobject("swap\\ arr[j]\\ and\\ arr[j+1]",tex_to_color_map={"swap":GREEN, "arr[j]\\ and\\ arr[j+1]":BLUE}).scale(0.8).to_edge(LEFT)
		swap.next_to(step3, DOWN).shift(RIGHT*0.5)
		end_inner_loop = TexMobject("End\\ of\\ Inner\\ Loop").scale(0.8).next_to(swap, DOWN).shift(LEFT*1.9)
		end_outer_loop = TexMobject("End\\ of\\ Outer\\ Loop").scale(0.8).next_to(end_inner_loop, DOWN).to_edge(LEFT)

		self.wait(1.5)
		self.play(Write(step3))
		self.wait(1)
		self.play(Write(swap))
		self.wait(5.5)
		self.play(Write(step1),Write(end_outer_loop))
		self.wait(6.5)
		self.play(Write(step2),Write(end_inner_loop))
		self.wait(13)
		return ((step2,step3,swap,end_inner_loop))

	def show_time_complexity(self,algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop):
		title = TextMobject('Time Complexity Analysis').scale(0.8).to_edge(RIGHT).shift(UP*2  + LEFT * 0.7)
		title_line = Line(title.get_right(), title.get_left()).next_to(title, DOWN)
		step_1 = TexMobject("(n-1)","+","(n-2)","+","(n-3)","+","...","+","1").scale(0.7).next_to(title_line, DOWN)
		step_2 = TexMobject("= \\frac{n(n-1)}{2} ").scale(0.8).next_to(step_1, DOWN).next_to(step_1, DOWN)
		step_3 = TexMobject("= \\frac{(n^2 - n)}{2}").scale(0.8).next_to(step_2, DOWN).next_to(step_2, DOWN)
		step_4 = TexMobject("= \\ O(n^2)").scale(0.8).next_to(step_3, DOWN).next_to(step_3, DOWN)
		inner_loop_group = VGroup(algo_step_2, algo_step_3, algo_swap, algo_end_inner_loop)

		self.play(Write(title), Write(title_line))
		self.wait()
		self.play(ShowPassingFlashAround(inner_loop_group))
		self.wait()
		for i in range(0,9,2):
			self.play(Transform(inner_loop_group.copy(),step_1[i:i+2]))
			self.wait(2)
		self.wait(4)
		self.play(ReplacementTransform(step_1.copy(), step_2))
		self.wait(6)
		self.play(ReplacementTransform(step_2.copy(),step_3)) 
		self.wait(6)
		self.play(ReplacementTransform(step_3.copy(), step_4))
		self.wait(3)

class Thumbnail(Scene):
	def construct(self):
		title = TextMobject('Bubble Sort Simulation').scale(1.5).to_edge(UP)
		title_line = Line(title.get_right(), title.get_left(), buff=0).next_to(title, DOWN)
		self.add(title, title_line)
		self.DrawPartitionLine(title_line)
		self.write_algo()


	def DrawPartitionLine(self, title_line):
		partition_line = Line(title_line.get_center(), DOWN*3)
		self.add(partition_line)

	def write_algo(self):
		step1 =  TexMobject("Loop\\ for\\ i=0\\ to\\ i=N-1",tex_to_color_map={"for":GREEN, "i=0":YELLOW,"i=N-1":RED}).scale(0.8).to_edge(LEFT)
		step1.shift(UP*1.5)
		step2 =  TexMobject("Loop\\ for\\ j=0\\ to\\ j=N-i-1", tex_to_color_map={"for":GREEN, "j=0":YELLOW,"j=N-i-1":RED}).scale(0.8)
		step2.next_to(step1, DOWN).shift(RIGHT*0.5)
		step3 = TexMobject("if\\ arr[j]\\ >\\ arr[j+1]:", tex_to_color_map={"if":GREEN, "arr[j]\\ >\\ arr[j+1]": BLUE}).scale(0.8)
		step3.next_to(step2, DOWN).shift(RIGHT*0.5)
		swap = TexMobject("swap\\ arr[j]\\ and\\ arr[j+1]",tex_to_color_map={"swap":GREEN, "arr[j]\\ and\\ arr[j+1]":BLUE}).scale(0.8).to_edge(LEFT)
		swap.next_to(step3, DOWN).shift(RIGHT*0.5)
		end_inner_loop = TexMobject("End\\ of\\ Inner\\ Loop").scale(0.8).next_to(swap, DOWN).shift(LEFT*1.9)
		end_outer_loop = TexMobject("End\\ of\\ Outer\\ Loop").scale(0.8).next_to(end_inner_loop, DOWN).to_edge(LEFT)

		self.add(step1)
		self.add(step2)
		self.add(step3)
		self.add(swap)
		self.add(end_inner_loop)
		self.add(end_outer_loop)
