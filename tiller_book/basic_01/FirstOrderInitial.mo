model FirstOrder
  Real x;
initial equation
  x = 2;
equation
  der(x) = 1 - x;
end FirstOrder;
