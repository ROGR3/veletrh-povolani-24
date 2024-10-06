from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock

from finished_functions.campaigns_sorter import CampaignsSorter
from helpers import Pacer, Campaign, RandomProbabilityGenerator


class TestCampaignsSorter(TestCase):
    def setUp(self) -> None:
        self.__pacer = Mock(Pacer)
        self.__pacer.get_delivery_indicator.side_effect = [0.5, 0.2, 0.1, 0.3]
        self.__random_generator = Mock(RandomProbabilityGenerator)
        self.__sorter = CampaignsSorter(self.__pacer, self.__random_generator)

    # - When asked to sort campaigns
    # -- And campaigns are guaranteed
    # -- And all campaigns have different priority
    # --- It should return campaigns sorted by priority first
    def test_sort_campaigns_by_priority(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="3", priority=2),
            self.create_campaign(campaign_id="1", priority=20),
            self.create_campaign(campaign_id="2", priority=15),
        ]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "1"
        assert sorted_campaigns[1].id == "2"
        assert sorted_campaigns[2].id == "3"

    # - When asked to sort campaigns
    # -- And campaigns are guaranteed
    # -- And some campaigns have same priority
    # --- It should return campaigns sorted by delivery indicator
    def test_sort_campaigns_by_delivery_indicator(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="3", priority=2),
            self.create_campaign(campaign_id="1", priority=2),
            self.create_campaign(campaign_id="2", priority=15),
            self.create_campaign(campaign_id="4", priority=15),
        ]
        self.__pacer.get_delivery_indicator.side_effect = [0.5, 0.3, 0.7, 0.9]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "2"
        assert sorted_campaigns[1].id == "4"
        assert sorted_campaigns[2].id == "1"
        assert sorted_campaigns[3].id == "3"

    # - When asked to sort campaigns
    # -- And campaigns are guaranteed
    # -- And priority also delivery indicator are same
    # --- It should return campaigns sorted by CPM
    def test_sort_campaigns_by_cpm(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="2", priority=2, cpm=3.0),
            self.create_campaign(campaign_id="1", priority=2, cpm=1.0),
            self.create_campaign(campaign_id="3", priority=2, cpm=2.0),
        ]
        self.__pacer.get_delivery_indicator.side_effect = [0.7, 0.5, 0.5]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "3"
        assert sorted_campaigns[1].id == "1"
        assert sorted_campaigns[2].id == "2"

    # - When asked to sort campaigns
    # -- And campaigns are guaranteed
    # -- And all criteria are the same
    # --- It should return campaigns randomly sorted
    def test_sort_campaigns_randomly(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="1", priority=10, cpm=3.0),
            self.create_campaign(campaign_id="2", priority=10, cpm=3.0),
            self.create_campaign(campaign_id="3", priority=2, cpm=3.0),
            self.create_campaign(campaign_id="4", priority=2, cpm=3.0),
        ]
        self.__random_generator.generate.side_effect = [0.1, 0.7, 0.4, 0.8]
        self.__pacer.get_delivery_indicator.side_effect = [0.5, 0.5, 0.5, 0.5]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "2"
        assert sorted_campaigns[1].id == "1"
        assert sorted_campaigns[2].id == "4"
        assert sorted_campaigns[3].id == "3"

    # - When asked to sort campaigns
    # -- And campaigns are unguaranteed
    # -- And all campaigns have different priority
    # --- It should return campaigns sorted by priority first
    def test_sort_unguaranteed_campaigns_by_priority(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="2", priority=0),
            self.create_campaign(campaign_id="1", priority=1),
        ]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "1"
        assert sorted_campaigns[1].id == "2"

    # - When asked to sort campaigns
    # -- And campaigns are unguaranteed
    # -- And priority is same
    # --- It should return campaigns sorted by CPM
    def test_sort_unguaranteed_campaigns_by_cpm(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="2", priority=0, cpm=3.0),
            self.create_campaign(campaign_id="1", priority=0, cpm=1.0),
            self.create_campaign(campaign_id="3", priority=0, cpm=2.0),
        ]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "2"
        assert sorted_campaigns[1].id == "3"
        assert sorted_campaigns[2].id == "1"

    # - When asked to sort campaigns
    # -- And campaigns are unguaranteed
    # -- And priority and cpm are same
    # --- It should return campaigns sorted by delivery Indicator
    def test_sort_unguaranteed_campaigns_by_delivery_indicator(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="1", priority=0, cpm=1.0),
            self.create_campaign(campaign_id="2", priority=0, cpm=1.0),
            self.create_campaign(campaign_id="3", priority=1, cpm=2.0),
            self.create_campaign(campaign_id="4", priority=1, cpm=2.0),
        ]

        self.__pacer.get_delivery_indicator.side_effect = [0.5, 0.3, 0.7, 0.9]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "3"
        assert sorted_campaigns[1].id == "4"
        assert sorted_campaigns[2].id == "2"
        assert sorted_campaigns[3].id == "1"

    # - When asked to sort campaigns
    # -- And campaigns are guaranteed
    # -- And all criteria are the same
    # --- It should return campaigns randomly sorted
    def test_sort_unguaranteed_campaigns_randomly(self) -> None:
        campaigns = [
            self.create_campaign(campaign_id="1", priority=0, cpm=3.0),
            self.create_campaign(campaign_id="2", priority=0, cpm=3.0),
            self.create_campaign(campaign_id="3", priority=1, cpm=3.0),
            self.create_campaign(campaign_id="4", priority=1, cpm=3.0),
        ]
        self.__random_generator.generate.side_effect = [0.1, 0.7, 0.4, 0.8]
        self.__pacer.get_delivery_indicator.side_effect = [0.5, 0.5, 0.5, 0.5]

        sorted_campaigns = self.__sorter.get_sorted_campaigns(campaigns, datetime.now())

        assert sorted_campaigns[0].id == "4"
        assert sorted_campaigns[1].id == "3"
        assert sorted_campaigns[2].id == "2"
        assert sorted_campaigns[3].id == "1"

    def create_campaign(
        self, campaign_id: str, priority: int, cpm: float = 1.0
    ) -> Campaign:
        return Campaign(
            id=campaign_id,
            priority=priority,
            cpm=cpm,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
        )
