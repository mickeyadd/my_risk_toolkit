# Chapter - 1 Value at Risk and Other Risk Metrics  

## 1.1 An Overview of Market Risk Assessment  

  -  1.1.1 Risk Measurement in Banks  
  -  1.1.2 Risk Measurement in Portfolio Management  
  -  1.1.3 Risk Measurement in Large Corporations  

## 1.2 Downside and Quantile Risk Metrics  

  -  1.2.1 Semi-Standard Deviation and Second Order Lower Partial Moment  
  -  1.2.2 Other Lower Partial Moments  
  -  1.2.3 Quantile Risk Metrics  

## 1.3 Defining Value at Risk  

  -  1.3.1 Confidence Level and Risk Horizon  
  -  1.3.2 Discounted P&L  
  -  1.3.3 Mathematical Definition of VaR  

## 1.4 Foundations of Value-at-Risk Measurement  

  -  1.4.1 Normal Linear VaR Formula: Portfolio Level  
  -  1.4.2 Static Portfolios  
  -  1.4.3 Scaling VaR  
  -  1.4.4 Discounting and the Expected Return  

## 1.5 Risk Factor Value at Risk  

  -  1.5.1 Motivation  
  -  1.5.2 Normal Linear Equity VaR  
  -  1.5.3 Normal Linear Interest Rate VaR  

## 1.6 Decomposition of Value at Risk  

  -  1.6.1 Systematic and Specific VaR  
  -  1.6.2 Stand-alone VaR  
  -  1.6.3 Marginal and Incremental VaR  

## 1.7 Risk Metrics Associated with Value at Risk  

  -  1.7.1 Benchmark VaR  
  -  1.7.2 Conditional VaR: Expected Tail Loss and Expected Shortfall  
  -  1.7.3 Coherent Risk Metrics  

## 1.8 Introduction to Value-at-Risk Models  

  -  1.8.1 Normal Linear VaR  
  -  1.8.2 Historical Simulation  
  -  1.8.3 Monte Carlo Simulation  
  -  1.8.4 Case Study: VaR of the S&P 500 Index  

# Chapter - 2 Parametric Linear VaR Models  

## 2.1 Foundations of Normal Linear Value at Risk  

  -  2.1.1 Understanding the Normal Linear VaR Formula  
  -  2.1.2 Analytic Formula for Normal VaR when Returns are Autocorrelated  
  -  2.1.3 Systematic Normal Linear VaR  
  -  2.1.4 Stand-Alone Normal Linear VaR  
  -  2.1.5 Marginal and Incremental Normal Linear VaR  

## 2.2 Normal Linear Value at Risk for Cash-Flow Maps  

  -  2.2.1 Normal Linear Interest Rate VaR  
  -  2.2.2 Calculating PV01  
  -  2.2.3 Approximating Marginal and Incremental VaR  
  -  2.2.4 Disaggregating Normal Linear Interest Rate VaR  
  -  2.2.5 Normal Linear Credit Spread VaR  

## 2.3 Case Study: PC Value at Risk of a UK Fixed Income Portfolio  

  -  2.3.1 Calculating the Volatility and VaR of the Portfolio  
  -  2.3.2 Combining Cash-Flow Mapping with PCA  
  -  2.3.3 Advantages of Using PC Factors for Interest Rate VaR  

## 2.4 Normal Linear Value at Risk for Stock Portfolios  

  -  2.4.1 Cash Positions on a Few Stocks  
  -  2.4.2 Systematic and Specific VaR for Domestic Stock Portfolios  
  -  2.4.3 Empirical Estimation of Specific VaR  
  -  2.4.4 EWMA Estimates of Specific VaR  

## 2.5 Systematic Value-at-Risk Decomposition for Stock Portfolios  

  -  2.5.1 Portfolios Exposed to One Foreign Currency  
  -  2.5.2 Portfolios Exposed to Several Foreign Currencies  
  -  2.5.3 Interest Rate VaR of Equity Portfolios  
  -  2.5.4 Hedging the Risks of International Equity Portfolios  

## 2.6 Case Study: Normal Linear Value at Risk for Commodity Futures  

## 2.7 Student t Distributed Linear Value at Risk  

  -  2.7.1 Effect of Leptokurtosis and Skewness on VaR  
  -  2.7.2 Student t Linear VaR Formula  
  -  2.7.3 Empirical Examples of Student t Linear VaR  

## 2.8 Linear Value at Risk with Mixture Distributions  

  -  2.8.1 Mixture Distributions  
  -  2.8.2 Mixture Linear VaR Formula  
  -  2.8.3 Mixture Parameter Estimation  
  -  2.8.4 Examples of Mixture Linear VaR  
  -  2.8.5 Normal Mixture Risk Factor VaR  

## 2.9 Exponential Weighting with Parametric Linear Value at Risk  

  -  2.9.1 Exponentially Weighted Moving Averages  
  -  2.9.2 EWMA VaR at the Portfolio Level  
  -  2.9.3 RiskMetrics™ VaR Methodology  

## 2.10 Expected Tail Loss (Conditional VaR)  

  -  2.10.1 ETL in the Normal Linear VaR Model  
  -  2.10.2 ETL in the Student t Linear VaR Model  
  -  2.10.3 ETL in the Normal Mixture Linear VaR Model  
  -  2.10.4 ETL under a Mixture of Student t Distributions  

## 2.11 Case Study: Credit Spread Parametric Linear Value at Risk and ETL  

  -  2.11.1 The iTraxx Europe Index  
  -  2.11.2 VaR Estimates  

# Chapter - 3 Historical Simulation  

## 3.1 Properties of Historical Value at Risk  

  -  3.1.1 Definition of Historical VaR  
  -  3.1.2 Sample Size and Data Frequency  
  -  3.1.3 Power Law Scale Exponents  
  -  3.1.4 Case Study: Scale Exponents for Major Risk Factors  
  -  3.1.5 Scaling Historical VaR for Linear Portfolios  
  -  3.1.6 Errors from Square-Root Scaling of Historical VaR  
  -  3.1.7 Overlapping Data and Multi-Step Historical Simulation  

## 3.2 Improving the Accuracy of Historical Value at Risk  

  -  3.2.1 Case Study: Equally Weighted Historical and Linear VaR  
  -  3.2.2 Exponential Weighting of Return Distributions  
  -  3.2.3 Volatility Adjustment  
  -  3.2.4 Filtered Historical Simulation  

## 3.3 Precision of Historical Value at Risk at Extreme Quantiles  

  -  3.3.1 Kernel Fitting  
  -  3.3.2 Extreme Value Distributions  
  -  3.3.3 Cornish–Fisher Approximation  
  -  3.3.4 Johnson Distributions  

## 3.4 Historical Value at Risk for Linear Portfolios  

  -  3.4.1 Historical VaR for Cash Flows  
  -  3.4.2 Total, Systematic and Specific VaR of a Stock Portfolio  
  -  3.4.3 Equity and Forex VaR of an International Stock Portfolio  
  -  3.4.4 Interest Rate and Forex VaR of an International Bond Position  
  -  3.4.5 Case Study: Historical VaR for a Crack Spread Trader  

## 3.5 Estimating Expected Tail Loss in the Historical Value-at-Risk Model  

  -  3.5.1 Parametric Historical ETL  
  -  3.5.2 Empirical Results on Historical ETL  
  -  3.5.3 Disaggregation of Historical ETL  

# Chapter - 4 Monte Carlo VaR  

## 4.1 Basic Concepts  

  -  4.1.1 Pseudo-Random Number Generation  
  -  4.1.2 Low Discrepancy Sequences  
  -  4.1.3 Variance Reduction  
  -  4.1.4 Sampling from Univariate Distributions  
  -  4.1.5 Sampling from Multivariate Distributions  
  -  4.1.6 Introduction to Monte Carlo VaR  

## 4.2 Modelling Dynamic Properties in Risk Factor Returns  

  -  4.2.1 Multi-Step Monte Carlo  
  -  4.2.2 Volatility Clustering and Mean Reversion  
  -  4.2.3 Regime Switching Models  

## 4.3 Modelling Risk Factor Dependence  

  -  4.3.1 Multivariate Distributions for i.i.d. Returns  
  -  4.3.2 Principal Component Analysis  
  -  4.3.3 Behavioural Models  
  -  4.3.4 Case Study: Modelling the Price – Volatility Relationship  

## 4.4 Monte Carlo Value at Risk for Linear Portfolios  

  -  4.4.1 Algorithms for VaR and ETL  
  -  4.4.2 Cash-Flow Portfolios: Copula VaR and PC VaR  
  -  4.4.3 Equity Portfolios: ‘Crash’ Scenario VaR  
  -  4.4.4 Currency Portfolios: VaR with Volatility Clustering  


# Chapter - 5 Value at Risk for Option Portfolios  

## 5.1 Risk Characteristics of Option Portfolios  

  -  5.1.1 Gamma Effects  
  -  5.1.2 Delta and Vega Effects  
  -  5.1.3 Theta and Rho Effects  
  -  5.1.4 Static and Dynamic VaR Estimates  

## 5.2 Analytic Value-at-Risk Approximations  

  -  5.2.1 Delta Approximation and Delta–Normal VaR  
  -  5.2.2 P&L Distributions for Option Portfolios  
  -  5.2.3 Delta–Gamma VaR  

## 5.3 Historical Value at Risk for Option Portfolios  

  -  5.3.1 VaR and ETL with Exact Revaluation  
  -  5.3.2 Dynamically Hedged Option Portfolios  
  -  5.3.3 Greeks Approximation  
  -  5.3.4 Historical VaR for Path-Dependent Options  
  -  5.3.5 Case Study: Historical VaR for an Energy Options Trading Book  

## 5.4 Monte Carlo Value at Risk for Option Portfolios  

  -  5.4.1 Monte Carlo VaR and ETL with Exact Revaluation  
  -  5.4.2 Risk Factor Models for Simulating Options VaR  
  -  5.4.3 Capturing Non-normality and Non-linearity  
  -  5.4.4 Capturing Gamma, Vega and Theta Effects  
  -  5.4.5 Path Dependency  
  -  5.4.6 Option Portfolios with a Single Underlying  
  -  5.4.7 Option Portfolios with Several Underlyings  
  -  5.4.8 Case Study: Monte Carlo VaR for an Energy Options Trading Book  


# Chapter - 6 Risk Model Risk  

## 6.1 Sources of Risk Model Risk  

  -  6.1.1 Risk Factor Mapping  
  -  6.1.2 Risk Factor or Asset Returns Model  
  -  6.1.3 VaR Resolution Method  
  -  6.1.4 Scaling  

## 6.2 Estimation Risk  

  -  6.2.1 Distribution of VaR Estimators in Parametric Linear Models  
  -  6.2.2 Distribution of VaR Estimators in Simulation Models  

## 6.3 Model Validation  

  -  6.3.1 Backtesting Methodology  
  -  6.3.2 Guidelines for Backtesting from Banking Regulators  
  -  6.3.3 Coverage Tests  
  -  6.3.4 Backtests Based on Regression  
  -  6.3.5 Backtesting ETL Forecasts  
  -  6.3.6 Bias Statistics for Normal Linear VaR  
  -  6.3.7 Distribution Forecasts  
  -  6.3.8 Some Backtesting Results  

# Chapter - 7 Scenario Analysis and Stress Testing  

## 7.1 Scenarios on Financial Risk Factors  

  -  7.1.1 Broad Categorization of Scenarios  
  -  7.1.2 Historical Scenarios  
  -  7.1.3 Hypothetical Scenarios  
  -  7.1.4 Distribution Scenario Design  

## 7.2 Scenario Value at Risk and Expected Tail Loss  

  -  7.2.1 Normal Distribution Scenarios  
  -  7.2.2 Compound Distribution Scenario VaR  
  -  7.2.3 Bayesian VaR  

## 7.3 Introduction to Stress Testing  

  -  7.3.1 Regulatory Guidelines  
  -  7.3.2 Systemic Risk  
  -  7.3.3 Stress Tests Based on Worst Case Loss  

## 7.4 A Coherent Framework for Stress Testing  

  -  7.4.1 VaR Based on Stressed Covariance Matrices  
  -  7.4.2 Generating Hypothetical Covariance Matrices  
  -  7.4.3 Stress Tests Based on Principal Component Analysis  
  -  7.4.4 Modelling Liquidity Risk  
  -  7.4.5 Incorporating Volatility Clustering  


# Chapter - 8 Capital Allocation  

## 8.1 Minimum Market Risk Capital Requirements for Banks  

  -  8.1.1 Basel Accords  
  -  8.1.2 Banking and Trading Book Accounting  
  -  8.1.3 Regulatory Framework for Market Risk  
  -  8.1.4 Internal Models  
  -  8.1.5 Standardized Rules  
  -  8.1.6 Incremental Risk Charge  

## 8.2 Economic Capital Allocation  

  -  8.2.1 Measurement of Economic Capital  
  -  8.2.2 Banking Applications of Economic Capital  
  -  8.2.3 Aggregation Risk  
  -  8.2.4 Risk Adjusted Performance Measures  
  -  8.2.5 Optimal Allocation of Economic Capital  