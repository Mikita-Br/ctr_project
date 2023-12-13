from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = 'CatboostClassifier'
    n_estimators: int = field(default=100)
    learning_rate: float = field(default=0.05)
    num_boost_round: int = 100
    depth: int = field(default=5)
    bagging_temperature: float = field(default=0.2)
    random_state: int = field(default=42)
