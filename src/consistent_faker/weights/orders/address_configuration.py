"""
Default weights for address configuration. These weights are used to randomly
generate billing and shipping addresses withinm the Fake order object
"""
DEFAULT_ADDRESS_CONFIGURATION_WEIGHTS = {
    "usr_default": 0.8,
    "usr_random": 0.15,
    "all_random": 0.05,
}
