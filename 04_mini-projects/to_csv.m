FileData = load('beta.mat');
csvwrite('beta.csv', FileData.ans);

FileData = load('psi.mat');
csvwrite('psi.csv', FileData.ans);

FileData = load('wheel_angle.mat');
csvwrite('wheel_angle.csv', FileData.ans);