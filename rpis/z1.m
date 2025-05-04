function y = z1(x, df1, df2)
    N = 1000000;
    B = gamma(df1/2) * gamma(df2/2) / gamma((df1+df2) / 2);
    c = (df1/df2)^(df1/2) / B;
    f = @(t) c * t.^(df1/2 - 1) .* (1 + (df1/df2)*t).^(-(df1+df2)/2);
    t = linspace(0, x, N+1);
    h = x / N;
    integral_val = h * ( sum(f(t)) - 0.5*(f(t(1))) + f(t(end)) );
    y = integral_val;
end