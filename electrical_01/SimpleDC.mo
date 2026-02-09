model SimpleDC
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;
  import Modelica.Electrical.Analog.Interfaces.*;

  ConstantVoltage V(V = 10);
  Resistor R(R = 5);
  Ground G;
equation
  connect(V.p, R.p);
  connect(R.n, V.n);
  connect(V.n, G.p);
end SimpleDC;
