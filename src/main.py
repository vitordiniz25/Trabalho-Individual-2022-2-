import os

from src.parser.YAML_parser import YAMLParser
from src.parser.feature_engineering_parser import FeatureEngineeringParser
from src.parser.model_parser import ModelParser


def get_config():
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineeringParser
    modelParser = ModelParser

    for file in os.listdir('src/yamls'):
        filepath = os.path.join('src/yamls', file)
        config = initialParser(filepath).parse()

        features_configs, columns_set_alias = featureEngineringParser(
            filepath).parse(config['feature_engineering'])
        del config['feature_engineering']

        model_configs = modelParser(columns_set_alias).parse(config['model'])
        del config['model']

        print("FEATURES")
        print(features_configs)
        print(3*'\n')
        print(20*'-')
        print(3*'\n')
        print(model_configs)


get_config()
