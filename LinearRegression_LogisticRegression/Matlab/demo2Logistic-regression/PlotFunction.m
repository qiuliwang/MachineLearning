function PlotFunction(xStart,xend)
   x = [-3;-2;-1;0;1;2;3];
   y = [0.01;0.05;0.3;0.45;0.8;1.1;0.99];
   plot(x,y,'rx','MarkerSize',10)
   hold on
   x_co = xStart:0.1:xend;
   theta = [0.28552;1.78148];
   y_co = h_func(x_co,theta);
   plot(x_co,y_co);
   hold off;
 end