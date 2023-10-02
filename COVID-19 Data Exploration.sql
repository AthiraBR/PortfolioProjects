
/*
* COVID-19 Data Exploration 
* Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types
* Dataset used: https://ourworldindata.org/covid-deaths
*/

-- Covid Deaths DataSet
SELECT *
FROM Portfolio..CovidDeaths
Where continent is not null
ORDER BY 3, 4

-- Covid Vaccinations DataSet
SELECT *
FROM Portfolio..CovidVaccinations
Where continent is not null
ORDER BY 3, 4

-- Select Data that we are going to be starting with
Select Location, date, total_cases, new_cases, total_deaths, population
from Portfolio..CovidDeaths
ORDER BY 1, 2

--Total Cases vs Total Deaths
--shows likelihood of dying in your country , say India
Select Location, date, total_cases, total_deaths
,(CONVERT(float,total_deaths)/NULLIF(CONVERT(FLOAT,total_cases),0))*100 as DeathPercenatge
from Portfolio..CovidDeaths where location like '%india%'
ORDER BY 1, 2

--Total cases vs Population
-- Shows what percentage of population infected with Covid
Select Location, date, total_cases, population
,(CONVERT(float,total_cases)/NULLIF(CONVERT(FLOAT,population),0))*100 as DeathPercenatge
from Portfolio..CovidDeaths where location like '%india%'
ORDER BY 1, 2

-- Countries with Highest Infection Rate compared to Population
Select Location, population, MAX(total_cases) as HighestInfectionCount
,MAX((CONVERT(float,total_cases)/NULLIF(CONVERT(FLOAT,population),0)))*100 as PercenatgePopulationInfected
from Portfolio..CovidDeaths 
group by Location, population
ORDER BY PercenatgePopulationInfected desc

-- Countries with Highest Death Count per Population
Select Location, MAX(cast(total_deaths as int)) as TotalDeathCounts
from Portfolio..CovidDeaths 
Where continent is not null
group by Location
ORDER BY TotalDeathCounts desc


--LET'S BREAK BY CONTINENT

--Showing the continent with highest death count per population
Select continent, MAX(cast(total_deaths as int)) as TotalDeathCounts
from Portfolio..CovidDeaths 
Where continent is not null
group by continent
ORDER BY TotalDeathCounts desc


--Breaking to GLOBAL NUMBERS
Select SUM(cast(new_cases as int)) as total_cases, SUM(cast(new_deaths as int)) as total_deaths,
SUM(cast(new_deaths as float))/SUM(cast(new_cases as float)) *100 as DeathPercentage
From Portfolio..CovidDeaths
order by 1,2

---Total Population vs Vaccination
-- Shows Percentage of Population that has recieved at least one Covid Vaccine
select de.continent, de.location, de.population, va.new_vaccinations
,SUM(cast(va.new_vaccinations as int)) OVER (Partition by de.location Order by de.location, de.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths de
Join Portfolio..CovidVaccinations va
on  de.location = va.location
and de.date = va.date
where de.continent is not null
order by 2,3


--USE CTE to perform Calculation on Partition By in previous query
With PopvsVac(continent, location, date,population, new_vaccinations,RollingPeopleVaccinated)
as
(
select de.continent, de.location, de.date, de.population, va.new_vaccinations
,SUM(cast(va.new_vaccinations as float)) OVER (Partition by de.location Order by de.location, de.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths de
Join Portfolio..CovidVaccinations va
on  de.location = va.location
and de.date = va.date
where de.continent is not null
)
select *, (RollingPeopleVaccinated/ nullif (cast(population as float),0) *100) as PercentageofPeopleVaccinated
from PopvsVac


--USE TEMP Table to perform Calculation on Partition By in previous query
DROP Table if exists #PercentageofPeopleVaccinated
Create table #PercentageofPeopleVaccinated(
continent nvarchar(220),
location nvarchar(220), 
date varchar(50),
population varchar(50), 
new_vaccinations varchar(50),
RollingPeopleVaccinated varchar(50)
)

Insert into #PercentageofPeopleVaccinated

select de.continent, de.location, de.date, de.population, va.new_vaccinations
,SUM(cast(va.new_vaccinations as float)) OVER (Partition by de.location Order by de.location, de.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths de
Join Portfolio..CovidVaccinations va
on  de.location = va.location
and de.date = va.date

Select *, (RollingPeopleVaccinated/nullif (cast(population as float),0) *100)
From #PercentageofPeopleVaccinated


-- Creating View to store data for later visualizations
Create View PercentageofPeopleVaccinated AS 
select de.continent, de.location, de.population, va.new_vaccinations
,SUM(cast(va.new_vaccinations as int)) OVER (Partition by de.location Order by de.location, de.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths de
Join Portfolio..CovidVaccinations va
on  de.location = va.location
and de.date = va.date
where de.continent is not null
