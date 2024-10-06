from datetime import datetime
from typing import List, Tuple

from helpers import Pacer, Campaign, RandomProbabilityGenerator


class CampaignsSorter:
    def __init__(
        self,
        pacer: Pacer,
        random_generator: RandomProbabilityGenerator,
    ) -> None:
        self.__pacer = pacer
        self.__random_generator = random_generator

    def get_sorted_campaigns(
        self, campaigns: List[Campaign], current_simulation_date: datetime
    ) -> List[Campaign]:

        return sorted(
            campaigns,
            key=lambda campaign: self.__get_campaign_sort_key(
                campaign, current_simulation_date
            ),
            reverse=True,
        )

    def __get_campaign_sort_key(
        self, campaign: Campaign, current_simulation_date: datetime
    ):
        delivery_indicator_sort_key = -self.__pacer.get_delivery_indicator(
            campaign, current_simulation_date
        )

        if self.__is_unguaranteed_campaign(campaign):
            return (
                campaign.priority,
                campaign.cpm,
                delivery_indicator_sort_key,
                self.__random_generator.generate(),
            )

        return (
            campaign.priority,
            delivery_indicator_sort_key,
            campaign.cpm,
            self.__random_generator.generate(),
        )

    def __is_unguaranteed_campaign(self, campaign: Campaign) -> bool:
        return campaign.priority < 2
