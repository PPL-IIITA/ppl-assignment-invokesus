# PPL-Assignment

## Souvik Sen - IIT2015505

### Contents
* [Build details](#build-details)
* [Deployment and Testing](#deployment-and-testing)
* [Documentation](https://ppl-iiita.github.io/ppl-assignment-invokesus/docs/html/index.html)
* [Class Diagrams](#class-diagrams)
* [Tools Used](#tools-used)  

#### Build Details
Developed and Tested on:  

| *OS* | macOS Sierra |
| --- | --- |
| *Distribution* | - |
| *Version* | 10.12.3 |
| *g++ Version* | g++ linked to clang by Xcode |  
| *Xcode Version* | 8.1 (8B62) |  
| *Apple LLVM Version* | 8.0.0 (clang-800.0.42.1) |
| *Documentation Generator* | Doxygen, Pyreverse |

#### Deployment and Testing
Clone this repository:
```
$ git clone https://github.com/PPL-IIITA/ppl-assignment-invokesus
```

Change to repository's directory:
```
$ cd ppl-assignment-invokesus
```
**To generate new testing data**

```
$python3 tester.py
```
#### Question 1:
**To form Couples from the generated test data**

```
$python3 q1.py
```
#### Question 2:
**To perform gifting and to find the  happiest and most compatible k couples**

```
$python3 q2.py
```

#### Question 4:
**To break up k couples and let the girls get new boyfriends**
```
$python3 q4.py
```
#### Question 5:
**To allow multiple algorithms for selection of Partner**
```
$python3 q5.py
```
#### Question 6:
**Makes Valentine's Day happen k days in a month. After which couples may break up and form new couples**
```
$python3 q6.py
```

**To view the logs**

```
$cat logs.txt
```

**To view docs**

To manually access documentation offline, all the HTML files of the documentation have been included in `./docs` directory.
Run any web server in this directory and open docs/index.html in any browser to view the documentation.


**To view the class diagram**

Open the `./class_diagram.png` file

#### Tools Used
Automatic documentation generation: Doxygen  
Class diagram generation: Pyreverse
