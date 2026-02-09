model RCCircuit
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;

  VoltageSource V(V = 5);
  //ConstantVoltage V(V = 10);
  Resistor R(R = 1e3);
  Capacitor C(C = 1e-6);
  Ground G;
equation
  connect(V.p, R.p);
  connect(R.n, C.p);
  connect(C.n, V.n);
  connect(V.n, G.p);
end RCCircuit;
