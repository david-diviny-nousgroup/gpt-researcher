from typing import TypedDict, List, Annotated
import operator


class ResearchState(TypedDict):
    task: dict
    initial_research: str
    sections: List[str]
    research_data: List[dict]
    # Report layout
    title: str
    headers: dict
    date: str
    executive_summary: str
    discussion: str
    implications:str
    sources: List[str]
    report: str


