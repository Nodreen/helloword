function [dk]=armijo( x0,s0)
%Çó²½³¤
    beat=0.5;sigma=0.2;
    d0=1;m=0;mk=0;
    f0=limin(x0);
    g0=grad(x0);
    xk=x0+d0*s0;
    fk=limin(xk);
gk=grad(xk);
dk=beat^m;
q1=f0-fk+sigma*dk*g0'*s0;
m=0;mmax=30;
while m<=mmax
      if q1>=0
          mk=m;break;
      else
        m=m+1;
        dk=beat^m;
        xk=x0+dk*s0;
        fk=limin(xk);
        q1=f0-fk+sigma*dk*g0'*s0;
      end
end
      dk=beat^mk;
end
