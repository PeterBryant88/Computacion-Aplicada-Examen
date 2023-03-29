% Definir la matriz de coeficientes y el vector de términos independientes
coef = [0.25 0.15 0; 0.45 0.5 0.75; 0.3 0.35 0.25];
inde = [1.5; 5; 3];

% Resolver el sistema de ecuaciones utilizando la función linsolve
x = linsolve(coef,inde);

% Mostrar la solución
disp('La solución del sistema de ecuaciones es:');
fprintf('Fertilizante A: %.2f \n', x(1));
fprintf('Fertilizante B: %.2f \n', x(2));
fprintf('Fertilizante C: %.2f \n', x(3));