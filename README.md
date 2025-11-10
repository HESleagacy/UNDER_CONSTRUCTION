# HESlegacy – California Housing Price Prediction API

**Model_finished**  
**CombinedAttributesAdder INCLUDED**  
**Production-Ready FastAPI**  
**Zero Pickle Errors**  
**Deployed in 2 minutes**

---

### Winner Model Stats
- **Algorithm**: RandomForestRegressor (GridSearchCV tuned)
- **Best Params**: `n_estimators=30`, `max_features=8`
- **Test RMSE**: ~48,000 USD
- **95% Confidence**: ± $3,800
- **Custom Features**: `rooms_per_household`, `population_per_household`, `bedrooms_per_room`

---

This work draws inspiration and guidance from the book  
**_Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow_**  
by **Aurélien Géron**.


---

### API Endpoint
```bash
POST /predict

