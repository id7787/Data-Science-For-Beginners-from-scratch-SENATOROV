"""Урок по математике."""

# 17.02.2025.
#
# "supervise learning" - обучение с учителем.
# есть data, ничего не размечаем, обучаемся по target.
#
# regression is a process for finding the relationship between the input data and output data.
# training data.
#
# y_n = f(x_n).
#
# a regression problem is about finding the best approximation to the input-output relationship of the data.
#
# The idea of regression is to add a structure to the problem; lets find g_0(.);
# this proxy g_0(.) takes a certain parametric form, we can postulate that (x_n,y_n)
# has  a linear relationship so g_0(x_n) = θ_1*x_n + θ_0, for n = 1, ... N; slope θ_1 and y-intercept = θ_0;
# where θ_1 and θ_0 - the parameter of model f.
#
# e_n - the 'error' between our model and real data.
# e_n = y_n - g_θ(x_n), for n = 1, ... N.
#
# the purpose of regression is to find the best θ such that the error is minimized.
