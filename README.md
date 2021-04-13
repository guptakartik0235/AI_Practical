
# <ins>Ai Practical </ins>


## **Introduction** # 
Hey there!
I am Kartik Gupta & this is my Repository with 
* 9 python Basic codes  
* Shape Detector - Intermediate Level

## **Requirements** #
* [Python](https://www.python.org/downloads/) version 3.6.0 or higher.
* [opencv](https://opencv.org/releases/) and [numpy](https://numpy.org/install/) modules installed
* Any IDE like:- ([Pycharm](https://www.jetbrains.com/pycharm/download/) or [Visual Studio code](https://code.visualstudio.com/download))

## **Codes** ##
1. [Triangle Can or Can't](1.py)
2. [The Tasks List Creator](2.py)
3. [The Image Displayer](3.py)
4. [The Work Place Teller](4.py)
5. [Rectangle or Square](5.py)
6. [Sum & Average Calculator](6.py)
7. [Image Blur](7.py)
8. [Image Resizer](8.py)
9. [Triangle Type](9.py)
10. [Shape Detector](ShapeDetector.py)

## **Explanation** ##
* ###  [1st Code](1.py)
**Inputs** - The code requires 3 sides of triangle as input. <br />
**Working** - The Code first stores the value of the 3 inputs in from of variables & then it compares every side using logic that the sum of two sides of triangles is never Greater than 3rd Side. 
<br />**Results** - The results tells us if these Dimensions could form a Triangle.<br />
![1st code img](https://user-images.githubusercontent.com/81790487/114462454-ae1cfb00-9c00-11eb-8b94-d71aad393f5f.PNG)
***
* ### [2nd Code](2.py)
**Inputs** - The code at first requires the no. of Task you want to do & then mention the tasks . <br />
**Working** - The Code uses a for loop as much times as you mentioned tasks to get your all Tasks . 
<br />**Results** - It make a list of all the tasks mentioned and print it for you .<br />

__The Output is as Shown in the Image Below__

![2nd code img](https://user-images.githubusercontent.com/81790487/114575148-862ca680-9c97-11eb-8554-203c502b558d.PNG)

***
* ### [3rd Code](3.py)
**Inputs** - The code requires an path of an Image as input to be added in the code. <br />
**Working** - The Code displays Images using functions of cv2 library. <br /> 
**Results** - The results displays us Image whose path we added in the code. <br />

__The Image Below Shows the result to the code__<br />  
![Lambo](https://user-images.githubusercontent.com/81790487/114567451-e2d89300-9c90-11eb-995a-0522d90ee4e4.jpg)<br />
Note:- You can add any Image of your choice by just adding its path or you can use the same Image & download it from [here](https://raw.githubusercontent.com/guptakartik0235/AI_Practical/main/lambo.jpg)  


***
* ### [4th Code](4.py)
**Inputs** - The code requires 2 inputs first one is age & second is Gender(But Input in M or F form) <br />
**Working** - The code uses the inputs & process them through various if-else conditions. <br /> 
**Results** - The results displays if we can work anywhere/Urban Areas/error(if you cant work Anywhere). <br />

__The Image Below Shows the result to the code__

![4th code img](https://user-images.githubusercontent.com/81790487/114577058-54b4da80-9c99-11eb-9398-9c33d106a86d.PNG)

***
* ### [5th Code](5.py)
**Inputs** - The code requires 2 inputs that are length and breadth of either a Rectangle or Square <br />
**Working** - The code uses the inputs & process them through **if-else condition** . <br /> 
**Results** - The results tells us if the figure is a Rectangle or Square alongwith its Area & Perimeter . <br />

__The Image Below Shows the result to the code__

![5th code img](https://user-images.githubusercontent.com/81790487/114578373-71054700-9c9a-11eb-84d8-b5b3ae937f35.PNG)

***
* ### [6th Code](6.py)
**Inputs** - The code requires input of the Length of list you want to create & also the list  <br />
**Working** - The code inputs the Length of list you mentioned and uses a **For-loop** to take inputs of the list. <br /> 
**Results** - The results prints the Average & Sum of the all elements of the list  . <br />

__The Image Below Shows the result to the code__

![6th code img](https://user-images.githubusercontent.com/81790487/114579410-73b46c00-9c9b-11eb-8ea1-6bf085c5a0e3.PNG)

***
* ### [7th Code](7.py)
**Inputs** - The code requires an Image path & inputs the Blur value. <br />
**Working** - The code uses the cv2 library & its Gaussian Blur function & processes Image . <br /> 
**Results** - The results displays the Image with the Blur . <br />

__The Image Below Shows the result to the code__

![7th code img](https://user-images.githubusercontent.com/81790487/114583886-aeb89e80-9c9f-11eb-9c5b-70a6fa3c8613.PNG)

**The value of Blur must be odd for Gaussian Blur function to work properly.**
***
* ### [8th Code](8.py)
**Inputs** - The code requires input of resized Width & Height of the Image. <br />
**Working** - The code uses the resize function of cv2 Library  . <br /> 
**Results** - The code Stores the input values and convert images to size as Input from the user. <br />

__The Image Below Shows the result to the code__

![8th code img](https://user-images.githubusercontent.com/81790487/114587858-aeba9d80-9ca3-11eb-997b-3fd4bdeb5757.PNG)

***
* ### [9th Code](9.py)
**Inputs** - The code requires input of length of various sides of Triangle . <br />
**Working** - The code uses simple else-if conditions. <br /> 
**Results** - The code differentiates between Scalene,Isoceles & Equilateral Triangle <br />

![9th code img](https://user-images.githubusercontent.com/81790487/114588863-c5152900-9ca4-11eb-82ca-e1e1b10fee0d.PNG)

***
## **[The code of ShapeDetector.py](ShapeDetector.py)** ##

 **The Code Inputs the Path of an Image which Contain various 2D - shapes & detect many shapes and also label them It Requires Cv2 & Numpy Library to be Installed.
I have also added a Picture to Repository named [shapes.png](https://github.com/guptakartik0235/AI_Practical/blob/main/shapes.PNG). Just download it and add its path in [ShapeDetector.py](ShapeDetector.py) at line no. 37**
**
## **Working Of The Project Take Place as Shown Below** ##
![shapedetector img](https://user-images.githubusercontent.com/81790487/114591544-a2384400-9ca7-11eb-9b9b-527e993dcd54.PNG)


***
## Credits  <br />
__Submitted By :- Kartik Gupta <br />
  Class :- 10th Bluebells <br />
  Roll no. :- 24 <br />
  Subject :- Artificial Intelligence <br />__
