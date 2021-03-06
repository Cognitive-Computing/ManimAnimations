from big_ol_pile_of_manim_imports import *
import numpy as np


class Insertion(Scene):
	def construct(self):
		array = self.get_array(6)
		values = [70,50,60,20,30,23]
		# values = list(np.random.randint(,90,7))
		value_group = self.put_values_in_array(array, values)
		title = TextMobject('Insertion Sort').scale(2).to_edge(UP)
		title_line = Line(title.get_right(), title.get_left()).scale(2).next_to(title, DOWN)
		self.play(Write(title), Write(title_line), runtime = 1.0)
		self.play(Write(array))
		self.wait()
		self.play(Write(VGroup(value_group)))
		self.show_insertion_simulation_actual(array,values, value_group)
		self.wait(2)

	def get_array_box(self):
		box = Rectangle()
		box.set_width(0.7)
		box.set_height(0.5)
		return box

	def get_array(self, size):
		return VGroup([self.get_array_box() for i in range(size)]).arrange_submobjects(RIGHT, buff=0)

	def put_values_in_array(self,array, values):
		values_group = [TextMobject(str(element)).scale(0.8).move_to(array[i].get_center()) for element, i in zip(values, list(range(len(values))))]
		return values_group

	def swap_value(self, i,j, array, values_group):
		value_i_transform = values_group[i].copy().move_to(array[j].get_center())
		value_j_transform = values_group[j].copy().move_to(array[i].get_center())
		# self.wait()
		# self.play(Transform(values_group[i], value_i_transform), Transform(values_group[j], value_j_transform), run_time=0.3)
		self.play(Swap(values_group[i], values_group[j]), runtime=0.3)


	# def show_insertion_simulation(self,array,values, values_group):
	# 	array1 = array.copy().set_color(RED)
	# 	line = Line(array[0].get_top(), array[0].get_bottom()).shift(RIGHT*0.5).scale(3).set_color(BLUE + GREEN)
	# 	line.set_stroke(width=3)
	# 	self.play(GrowFromCenter(line))
	# 	for i in range(1,len(values)):
	# 		values_key = values[i]
	# 		values_group_key = values_group[i]
	# 		j = i - 1
	# 		flag = 0
	# 		while j >= 0 and values_key < values[j]:
	# 			flag = 1
	# 			array[i].set_fill(RED, opacity=0.3)
	# 			values[j+1] = values[j]
	# 			array[j].set_fill(BLUE, opacity=0.3)
	# 			j-=1
	# 			self.wait(1)
	# 			continue
	# 		values[j+1] = values_key
	# 		if flag ==1:
	# 			self.show_insertion(values_group, i,j, array)
	# 		values_group[j+1], values_group[i] = values_group_key, values_group[j+1]
	# 		self.play(line.move_to, array[i].get_right())
	# 	self.play(ShowPassingFlashAround(array1), run_time=2)
	# 	self.wait(2)



	# def show_insertion(self,values_group,i,j, array):
	# 	VGroup(array[j+1:i]).set_fill(BLACK, opacity=1)
	# 	array[i].set_fill(BLACK, opacity=1)
	# 	self.play(VGroup(values_group[i]).shift, DOWN*1, VGroup(values_group[j+1:i]).shift, RIGHT*1)
	# 	self.play(VGroup(values_group[i]).move_to, array[j+1].get_center())


	def show_insertion_simulation_actual(self,array,values, values_group):
		array1 = array.copy().set_color(RED)
		line = Line(array[0].get_top(), array[0].get_bottom()).shift(RIGHT*0.5).scale(3).set_color(BLUE + GREEN)
		line.set_stroke(width=3)
		brace1 = Brace(array[0:4], UP, buff = SMALL_BUFF)
		brace2 = Brace(array[4:], DOWN, buff = SMALL_BUFF)
		t1 = brace1.get_text("Sorted Part")
		t1.set_color(YELLOW)
		t2 = brace2.get_text("UnsortedPart")
		t2.set_color(RED)
		self.play(GrowFromCenter(line))

		array[1:].set_color(RED)

		for i in range(1,len(values)):
			array[i-1].set_color(YELLOW)
			array[i-1].set_fill(BLACK, opacity =1)
			values_key = values[i]
			values_group_key = values_group[i]
			j = i - 1
			flag = 0
			if i == 4:
				self.play(GrowFromCenter(brace1), Write(t1))
				self.wait(0.5)
				self.play(GrowFromCenter(brace2), Write(t2))
				self.wait(1.5)
				self.play(FadeOutAndShiftDown(brace1),FadeOutAndShiftDown(brace2),FadeOutAndShiftDown(t1),FadeOutAndShiftDown(t2))
			array[i].set_fill(BLUE, opacity=0.3)
			if values_key < values[j]:
				self.wait()
				array[i].set_fill(BLACK, opacity=1)
				self.play(VGroup(values_group[i]).shift, DOWN*1)
			

			while j >= 0 and values_key < values[j]:
				flag = 1
				values[j+1] = values[j]
				self.wait()
				array[j].set_fill(RED, opacity=0.3)

				self.wait(1)
				values_group[j+1] = values_group[j]
				self.shift_value(values_group,i,j,array)
				j-=1
				# self.shift_value(values_group,i,j,array)
				# values_group[j+1] = values_group[j]
				self.wait(1)
			values[j+1] = values_key
			values_group[j+1] = values_group_key

			if flag ==1:
				self.show_insertion_actual(values_group, i,j, array)
			# values_group[j+1], values_group[i] = values_group_key, values_group[j+1]
			values_group[j+1] = values_group_key
			self.play(line.move_to, array[i].get_right())
		array[5].set_color(YELLOW)
		array[5].set_fill(BLACK)

		self.play(FadeOutAndShiftDown(line))
		self.wait()
		self.play(ShowPassingFlashAround(array1), run_time=2)
		self.wait(2)

	def show_insertion_actual(self,values_group,i,j, array):
		self.play(VGroup(values_group[j+1]).move_to, array[j+1].get_center())

	def shift_value(self,values_group,i,j,array):
		array[j].set_fill(BLACK,opacity=1)
		self.play(VGroup(values_group[j]).shift, RIGHT*1)




class Introduction(Scene):
	def construct(self):
		text1 = TextMobject('Insertion Sort').scale(2).to_edge(UP)
		line1 = Line(text1.get_right(), text1.get_left(), buff=0).next_to(text1, DOWN)
		section1 = TextMobject('1. Techniques and Key Idea').scale(1).next_to(line1,DOWN).set_color(GREEN)
		section2 = TextMobject('2. Insertion Sort Simulation').scale(1).next_to(line1,DOWN).set_color(BLUE)
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

class Section2(Insertion,Scene):
	def construct(self):
		array = self.get_array(6)
		values = [70,50,60,20,30,23]
		title = TextMobject('Insertion Sort Algorithm').scale(1.5).to_edge(UP)
		title_line = Line(title.get_right(), title.get_left()).next_to(title, DOWN).set_color(BLUE,GREEN).set_stroke(width=2)
		self.partition_line = Line(title_line.get_center(), DOWN*3).set_color(BLUE,GREEN).set_stroke(width=2)
		array.next_to(title_line, DOWN * 3 ).to_edge(RIGHT)
		value_group = self.put_values_in_array(array, values)

		self.play(Write(title))
		self.play(GrowFromCenter(title_line))
		self.play(Write(self.partition_line))
		self.wait(2)

		step_lst = self.write_algo()
		self.wait()
		# self.play(Write(array))
		# self.play(Write(VGroup(value_group)))
		# self.show_insertion_simulation_actual(array,values,value_group)
		# self.wait(2)
		# self.play(FadeOutAndShiftDown(VGroup(array)), FadeOutAndShiftDown(VGroup(value_group)))
		self.time_complexity_analysis(step_lst)
		self.wait()



	def write_algo(self):
		step1 =  TexMobject("for\\ i=1\\ to\\ i<N-1",tex_to_color_map={"for":BLUE, "i=1":YELLOW,"i<N-1":RED}).scale(0.8).to_edge(LEFT)
		step1.shift(UP*1.9)
		step2 =  TexMobject("set\\ Temp\\ = \\arr[i]", tex_to_color_map={"set":BLUE, "Temp":YELLOW,"arr[i]":RED}).scale(0.8)
		step2.next_to(step1, DOWN).to_edge(LEFT*1.7)
		step3 = TexMobject("set\\ j\\ = \\i-1", tex_to_color_map={"set":BLUE, "j":YELLOW,"i-1":RED}).scale(0.8)
		step3.next_to(step2, DOWN).to_edge(LEFT*1.7)

		step4_color = {"while":BLUE, "Temp": YELLOW , 'and': BLUE, "j":YELLOW, "0":YELLOW, "arr[":YELLOW, "]":YELLOW}

		step4 = TexMobject("while\\ Temp<=arr[j] \\ and \\ j>=0",tex_to_color_map=step4_color).scale(0.8)
		step4.next_to(step3, DOWN).to_edge(LEFT*1.7)

		step4_a = TexMobject("set\\ arr[j+1]\\ = \\arr[j]", tex_to_color_map={"set":BLUE, "arr[j+1]":YELLOW,"arr[j]":RED}).scale(0.8)
		step4_a.next_to(step4, DOWN).to_edge(LEFT*2.4)

		step4_b = TexMobject("set\\ j\\ =\\ j-1", tex_to_color_map={"set":BLUE, "j":YELLOW,"j-1":RED}).scale(0.8)
		step4_b.next_to(step4_a,DOWN).to_edge(LEFT*2.4)

		step5 = TexMobject("set\\ arr[j+1]\\ = \\Temp", tex_to_color_map={"set":BLUE, "arr[j+1]":YELLOW,"Temp":RED}).scale(0.8)

		end_inner_loop = TexMobject("End\\ of\\ Inner\\ Loop").scale(0.8).next_to(step4_b, DOWN).to_edge(LEFT*1.7)
		step5.next_to(end_inner_loop, DOWN).to_edge(LEFT*1.7)
		end_outer_loop = TexMobject("End\\ of\\ Outer\\ Loop").scale(0.8).next_to(step5, DOWN).to_edge(LEFT)

		self.play(Write(step1))
		self.wait()
		self.play(Write(step2))
		self.wait()
		self.play(Write(step3))
		self.wait()
		self.play(Write(step4))
		self.wait()
		self.play(Write(step4_a))
		self.wait()
		self.play(Write(step4_b))
		self.wait()
		self.play(Transform(step4.copy(),end_inner_loop))
		self.wait()
		self.play(Write(step5))
		self.wait()
		self.play(Transform(step1.copy(), end_outer_loop))
		self.wait(2)
		return [step1,step2,step3,step4,step4_a,step4_b,step5,end_inner_loop,end_outer_loop]

	def time_complexity_analysis(self, steps):
		title_best = TextMobject("Best Case Time Complexity").scale(0.8).to_edge(RIGHT).shift(UP*2  + LEFT * 0.7)
		title_worst = TextMobject("Worst Case Time Complexity").scale(0.8).to_edge(RIGHT).shift(UP*2  + LEFT * 0.7)
		title_line = DashedLine(title_best.get_right(), title_best.get_left()).next_to(title_best, DOWN)
		frame_box1 = SurroundingRectangle(steps[3][2:], buff=.1).set_color('#007d7d').set_stroke(width=2)
		frame_box2 = SurroundingRectangle(steps[4], buff=.1).set_color('#007d7d').set_stroke(width=2)
		s4_line = Line(frame_box1.get_top(), title_line.get_center()).set_stroke(width =2).set_color('#007d7d')
		# s4_line_copy = s4_line.copy()
		s4a_line = Line(frame_box2.get_right(), title_line.get_center()).set_stroke(width =2).set_color('#007d7d')
		# s4a_line_copy = s4a_line.copy()
		best_case_step1 = TexMobject("= \\ N-1").next_to(title_line, DOWN)
		best_case_step2 = TexMobject("= \\Omega\\ (N)").next_to(best_case_step1, DOWN)

		worst_case_step1 = TexMobject("2(","1","+","2","+...","+","N-2","+","N-1",")").scale(0.8).next_to(title_line, DOWN)
		worst_case_step2 = TexMobject("= \\frac{n(n+1)}{2} ").scale(0.8).next_to(worst_case_step1, DOWN)
		worst_case_step3 = TexMobject("= \\frac{(N-1)(N-1+1)}{2}").scale(0.8).next_to(worst_case_step2, DOWN)
		worst_case_step3_transform  = TexMobject("= \\frac{2(N-1)(N-1+1)}{2}").scale(0.8).next_to(worst_case_step2, DOWN)
		worst_case_step4 = TexMobject("= \\ N(N-1)").scale(0.8).next_to(worst_case_step3, DOWN)
		worst_case_step5 = TexMobject("= \\ O(N^2)").scale(0.8).next_to(worst_case_step4, DOWN)

		self.wait()
		self.play(FadeOut(self.partition_line))
		self.play(Write(title_best), Write(title_line))
		self.wait(4)
		self.play(ShowCreation(frame_box1))
		self.wait()
		self.play(ReplacementTransform(frame_box1.copy(), frame_box2))
		self.wait()
		self.play(ShowCreationThenDestruction(s4_line),ShowCreationThenDestruction(s4a_line), run_time=2)
		self.wait(2)
		self.play(FadeOut(frame_box1),FadeOut(frame_box2))
		self.wait()
		self.play(ShowPassingFlashAround(steps[3][2:]))
		self.wait()
		self.play(ReplacementTransform(VGroup(steps[1:-1]).copy(), best_case_step1))
		self.wait()
		self.play(ReplacementTransform(best_case_step1.copy(), best_case_step2))
		self.wait()
		self.play(FadeOut(best_case_step1),FadeOut(best_case_step2))
		self.play(ReplacementTransform(title_best, title_worst))
		self.wait()
		self.play(ReplacementTransform(VGroup(steps[1:-1]).copy(), worst_case_step1[1:3]))
		self.wait()
		self.play(ReplacementTransform(VGroup(steps[1:-1]).copy(), worst_case_step1[3:5]))
		self.wait()
		self.play(ReplacementTransform(VGroup(steps[1:-1]).copy(), worst_case_step1[5:-1]))
		self.wait()
		self.play(Write(worst_case_step1[0]), Write(worst_case_step1[-1]))
		self.wait()
		self.play(ReplacementTransform(worst_case_step1.copy(), worst_case_step2))
		self.wait()
		self.play(ReplacementTransform(worst_case_step2.copy(), worst_case_step3))
		self.wait()
		self.play(ReplacementTransform(worst_case_step3, worst_case_step3_transform))
		self.wait()
		self.play(ReplacementTransform(worst_case_step3_transform.copy(), worst_case_step4))
		self.wait()
		self.play(ReplacementTransform(worst_case_step4.copy(), worst_case_step5))
		# self.play(ReplacementTransform(worst_case_step4.copy(), worst_case_step5))
		self.wait(2)

class Thumbnail(Scene):
	def construct(self):
		title = TextMobject("Insertion \\\\ Sort \\\\ Visualized").scale(2.5).to_edge(LEFT)
		self.add(title)





