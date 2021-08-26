# semaf-poc
SEMAF Flexible Semantic Mapping Framework Proof of Concept 

# Presentations and reports
* Flexible Semantic Mapping Framework [pdf](https://indico.fccn.pt/event/15/contributions/80/attachments/55/111/Breoder%20-%20SEMAF%20presentation%20eIRG%20v2.pdf)
* SEMAF final report [Zenodo](http://doi.org/10.5281/zenodo.4651421)

# Installation
Clone Apache Superset visualization framework and enable Apache Drill connection
```
git clone https://github.com/apache/superset
echo 'sqlalchemy-drill' > ./superset/docker/requirements-local.txt
docker-compose up
```

# Infrastructure
* Apache Superset
* Apache Drill
* MongoDB NoSQL database
* PostgresQL database
