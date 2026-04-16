# Ex. 1

Let $V$ and $W$ be vector spaces over a field $\mathbb{F}$ (in PDE use-case $\mathbb{R}$).  

An operator
$$
L : V \to W
$$
is called **linear** if for all $u, v \in V$ and all scalars $\alpha, \beta \in \mathbb{F}$, it satisfies:

1. **Additivity**: $L(u + v) = L(u) + L(v)$,
2. **Scaling**: $L(\alpha u) = \alpha L(u)$.

Or together:

$$
L(\alpha u + \beta v) = \alpha L(u) + \beta L(v)
$$

#### Given:
- $L u = u_x + x u_y$ (linear)
- $L u = u_x + u u_y$ (nonlinear)
- $L u = u_t + u_x + 1$ (nonlinear)
- $L u = u_x^2 + u_y^2 - 1$ (nonlinear)
