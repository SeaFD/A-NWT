SetFactory("OpenCASCADE");
// Parameters
param[0]= 4.22; // Length of the box in meters
param[1] = 0.15; // Width of the box in meters
param[2] = 1.8; // Height of the box in meters
param[3] = 0.15; // Radius of the semi-circle in meters
param[4] = 0.09;  // Initial drop height

// Define points
Point(1) = {0, 0, -param[2]/2-param[4], 0.05};
Point(2) = {param[0], 0, -param[2]/2-param[4], 0.05};
Point(3) = {param[0], param[1], -param[2]/2-param[4], 0.05};
Point(4) = {0, param[1], -param[2]/2-param[4], 0.05};
Point(5) = {0, 0, param[2]/2, 0.05};
Point(6) = {param[0], 0, param[2]/2, 0.05};
Point(7) = {param[0], param[1], param[2]/2, 0.05};
Point(8) = {0, param[1], param[2]/2, 0.05};

// Points for semi-circle
Point(9) = {0, 0, 0, 0.01}; // Center of semi-circle
Point(10) = {0, 0 , - param[3], 0.01}; // Start of semi-circle
Point(11) = {0, 0, param[3], 0.01}; // End of semi-circle
Point(12) = {0, param[1], 0, 0.01}; // Center of semi-circle
Point(13) = {0, param[1] , - param[3], 0.01}; // Start of semi-circle
Point(14) = {0, param[1], param[3], 0.01}; // End of semi-circle

Point(15) = {param[3], 0, 0, 0.01}; // Center of semi-circle
Point(16) = {param[3], param[1], 0, 0.01}; // Center of semi-circle


// Define lines for the box
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 5};
Line(9) = {1, 10};
//Line(10) = {10, 11};
Line(11) = {11, 5};
Line(12) = {2, 6};
Line(13) = {3, 7};
Line(14) = {4, 13};
Line(15) = {13, 14};
Line(16) = {14, 8};
Line(17) = {10, 13};
Line(18) = {11, 14};

// Define semi-circle
Circle(19) = {10, 9, 15};
Circle(37)={15, 9, 11};
Circle(20) = {13, 12, 16};
Circle(38) = {16, 12, 14};

// Define line loops and surfaces for the box
Line Loop(21) = {4,3,2,1};
Plane Surface(22) = {21};
Line Loop(23) = {5, 6, 7, 8};
Plane Surface(24) = {23};
Line Loop(25) = {1, 12, -5, -11, -37, -19, -9};
Plane Surface(26) = {25};
Line Loop(27) = {3, -13, -7, 16,  38, 20, 14};
Plane Surface(28) = {27};
Line Loop(29) = {2,13,-6,-12};
Plane Surface(30) = {29};
Line Loop(31) = {4,-14,17,9};
Plane Surface(32) = {31};
Line Loop(33) = {-18,11,-8,-16};
Plane Surface(34) = {33};

// Define line loop and surface for the semi-circle
Line Loop(35) = {-17,19,37,18,-38,-20};
Surface(36) = {35};




// Boundary conditions (named surfaces)
Physical Surface("back") = {28};  // set here patch name
Physical Surface("front")    = {26};  // set here patch name
Physical Surface("bottom")  = {22};  // set here patch name
Physical Surface("atmosphere")   = {24};  // set here patch name
Physical Surface("axis1")   = {32};  // set here patch name
Physical Surface("axis2")  = {34};  // set here patch name
Physical Surface("floatingBody")  = {36};  // set here patch name
Physical Surface("tankWall")  = {30};  // set here patch name

Mesh.StlOneSolidPerSurface = 2;


