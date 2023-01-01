DriCon: On-device Just-in-Time Context Characterization for Unexpected Driving Events

Driving is a complex task carried out under the influence of diverse spatial objects and their temporal interactions. Therefore, a sudden fluctuation in driving behavior can be due to either a lack of driving skill or the effect of various on-road spatial factors such as pedestrian movements, peer vehicles’ actions, etc. Therefore, understanding the context behind a degraded driving behavior just-in-time is necessary to ensure on-road safety. In this paper, we develop a system called DriCon that exploits the information acquired from a dashboard-mounted edge-device to understand the context in terms of micro-events from a diverse set of on-road spatial factors and in-vehicle driving maneuvers taken. DriCon uses the live in-house testbed and the largest publicly available driving dataset to generate human interpretable explanations against the unexpected driving events. Also it provides a better insight with an improved accuracy of 80% over 50 hours of driving data than the existing driving behavior characterization techniques.
Use the following commands in sequence to run the system.
python data_collect.py <file_name> ## Collect Data
python maneuvers.py <file_name> ## Feature Extraction
python script_vid.py <file_name> ## Preprocessing
We train our model using som_iter.py ## Running the model
