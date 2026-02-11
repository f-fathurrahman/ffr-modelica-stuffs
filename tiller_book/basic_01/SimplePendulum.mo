model SimplePendulum

  inner Modelica.Mechanics.MultiBody.World world;

  Modelica.Mechanics.MultiBody.Joints.Revolute revolute(
    phi(start = 0.5));

  Modelica.Mechanics.MultiBody.Parts.Body body(
    m = 1,
    I_11 = 0.1,
    I_22 = 0.1,
    I_33 = 0.1);

equation
  connect(world.frame_b, revolute.frame_a);
  connect(revolute.frame_b, body.frame_a);

end SimplePendulum;
