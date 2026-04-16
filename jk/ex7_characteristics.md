
# Ex. 7
TODO: solve each PDE using characteristic curves.

## Note on characteristics method

Assumption: Function $u:\mathbb{R}^2 \rightarrow \mathbb{R}$ in form of: $u = u(x(t),t)$.

Total time derivateve of $u$ is:

$$
\frac{d}{dt} u(x(t),t) = 
\frac{\partial u}{\partial t} \frac{dt}{dt}
+ \frac{\partial u}{\partial x} \frac{dx}{dt}
$$

Thus:

$$
\frac{du}{dt} = 
u_t
+ \frac{dx}{dt} u_x
$$

---
## (A)

$$
u_t + 10u_x = 0, \quad t>0,\; x\in\mathbb{R}, \quad u(x,0)=\frac{1}{1+x^2}
$$

Characteristics
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