function [PCC_all, SROCC_all] = evaluation(preds,dmos)
cnt1=1;
score = preds;
MOS =dmos;
avg_score=ones(73,1);
for cnt=1:220:length(score)
    avg_score(cnt1)=mean(score(cnt:cnt+219));
    cnt1=cnt1+1;
end

cnt2=1;
avg_MOS=ones(73,1);
for cnt=1:220:length(MOS)
    avg_MOS(cnt2)=mean(MOS(cnt:cnt+219));
    cnt2=cnt2+1;
end
avgScore=avg_score;
avgMOS=avg_MOS;

SROCC_all = corr(avgScore, avgMOS, 'type', 'Spearman')
PCC_all = calculatepearsoncorr(avgScore, avgMOS, 0)
end

function [linearcorr bestbeta bestquality] = calculatepearsoncorr(quality,humanscores,drawing)

x = quality; 
y = humanscores; 
bestbeta = zeros(5,1);
bestpcc = 0;
bestquality = quality;
itr =1;
for fact = 0.01:0.1:10
    itr = itr+1;
beta0 = [max(y) min(y) fact*mean(x) 1 0];
%[msg, msgid] = lastwarn
%s = warning('off','stats:nlinfit:IllConditionedJacobian');
warning off all
b_blur = nlinfit(x,y,@logistic_fun,beta0);
x_hat = logistic_fun(b_blur,x);
Correlation(itr) = corr(x_hat,y);
if Correlation(itr) > bestpcc
    bestpcc = Correlation(itr);
    bestbeta = b_blur;
    bestquality = x_hat;
end

end

linearcorr = max(Correlation);

if drawing
    figure;hold on;
    xline = [min(quality):0.01:max(quality)];
    yline = logistic_fun(bestbeta,xline);
    plot(xline,yline);
    plot(quality,humanscores,'*k');
    title(['PCC=' num2str(linearcorr)]);
end

function [L] = logistic_fun(beta,x)

L = beta(1)*(0.5-1./(1+exp(beta(2)*(x-beta(3))))) + beta(4)*x+beta(5);
end
end