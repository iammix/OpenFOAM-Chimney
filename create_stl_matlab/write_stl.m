clear all;
clc;

radius = 1.0;
height = 20.0;
number_z = 50;
nodes = 50;

r = radius * ones(1,nodes);
th = linspace(0, 2*pi, nodes);
z = linspace(0, height, number_z)';

[x,y] = pol2cart(th,r);

X = repmat(x,number_z,1);
Y = repmat(y,number_z,1);
Z = repmat(z,1,nodes);

x_c = zeros(1,nodes);
y_c = zeros(1,nodes);
z_c = repmat(height,1,nodes);

X = [X; x_c(1,:)];
Y = [Y; y_c(1,:)];
Z = [Z; z_c(1,:)];

surf2stl(['cylinder.stl'],X,Y,Z,'ascii')
