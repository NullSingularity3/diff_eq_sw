
# Ex. 7
TODO: solve each PDE using characteristic curves.

## Note on characteristics method 

Assumption: 
- Function $u:\mathbb{R}^2 \rightarrow \mathbb{R}$ in form of: $u = u(x(t),t)$.
- 1D, time dependent case

We calculate total time derivateve of $u$ (remember about chain rule):

$$
\frac{d}{dt} u(x(t),t) = \frac{\partial u}{\partial t} \frac{dt}{dt} + \frac{\partial u}{\partial x} \frac{dx}{dt}
$$

Thus:

$$
\frac{du}{dt} = u_t + \frac{dx}{dt} u_x
$$

For a PDE in gneral form of:

$$
u_t + a(x,t) u_x = b(x,t)
$$

We look for curves x(t) (called characteristics) along which the PDE becomes an ODE. Comparing total derivative with general form of PDE we get:

- $\frac{dx}{dt} = a(x,t)$
- $\frac{du}{dt} = b(x,t)$

By doing above we reduced PDE to set of ODEs. To obtain solution:
- Solve the first ODE to find characteristic curves $x(t)$. 
- Then solve the second ODE along those curves to obtain u.
- Initial conditions e.g. $u(x,0) = f(x)$ determine the constants.

---

## (A)

$$
u_t + 10u_x = 0, \quad t>0,\; x\in\mathbb{R}, \quad u(x,0)=\frac{1}{1+x^2}
$$

In our case:

- $\frac{dx}{dt} = 10$
- $\frac{du}{dt} = 0$


Characteristics:

$$
\frac{dx}{dt} = 10 \Rightarrow x - 10t = C
$$

General solution

$$
u(x,t) = f(x - 10t)
$$

Apply initial condition

$$
u(x,0) = f(x) = \frac{1}{1+x^2}
$$

Final answer

$$
u(x,t) = \frac{1}{1 + (x - 10t)^2}
$$
