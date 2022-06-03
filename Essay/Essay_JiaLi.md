# **The wide application of network science to contain COVID-19 featured with small-world phenomenon**

## **Introduction**

Covid-19 is the latest emerging pandemic humans suffer. Like other
transmitted diseases, the pathogen of Covid-19 spreads on our social
contact networks. The properties and structures of Covid-19 transmission
networks can truly impact the outcome of the pandemic, either long-term
existence or die out. Network science was formed only in the 21st
century. The research for networks can help with the analysis,
monitoring, simulation, and prediction of the pandemic. An important
concept in network science is the 'small world' property that exists in
real social networks. Most research relevant to Covid-19 is inevitably
connected to the small world property. This essay first explains the
small world concept, then reviews the advancement of social network in
the field of epidemic research, next focuses on the characteristics of
Covid-19 contact networks, the breakthroughs in modelling, and their
applications, and finally, give implications for Covid-19 containment
measurements.

## **Concept of small world**

We are all often surprised at finding a friend who is also the friend of
a friend. The surprise is from the assumption that one person's friend
circle is significantly smaller than the total population. The
characteristics of networks can be quantified by the network science
concept: distance or path length. While grid-like networks have a long
average path length, social networks have a short average length
(Barabási, 2014; Menczer et al., 2020).

The definition of the 'small world' is that "the distance between two
randomly chosen nodes in a network is short". Its manifestation in
social networks is the famous theory: six degrees of separation. Namely,
any two people in the world are connected within a very short social
distance consisting of acquaintances in the whole social network. Small
world phenomenon originates from random networks. A root fact is the
number of nodes at a distance d from a node increases exponentially with
d. For example, if ‹k› ≈ 1,000 (one person has 1000 acquaintances, a
common situation in the real world), the result is a billion individuals
at distance of two and almost the whole world's population at distance
of three. An experiment conducted by Milgram in the 1960s presented the
first empirical evidence of 'small world'. The subsequent experiments
suggested that 'Six' is just a symbolistic figure. In fact, the link
number in small worlds is approximately between 4 and 6. Mathematically,
'average path is short' means the average path length scales
logarithmically with the size of the network. In other words, the
average path length grows slowly as the size of the network grows, or
distances in a random network are orders of magnitude smaller than the
size of the network. Additionally, this character can be measured by
clustering coefficient (the number of triangles around a node).
Normally, the clustering coefficient of an entire network is large in
social networks (Barabási, 2014; Menczer et al., 2020).

Barabási (2014) and Menczer et al. (2020) suggested that real networks
are different from original random networks. The degree distribution of
random networks is approximated by the Poisson distribution, assuming
the network is sparse and \<k\> \<\< N. However, real networks are not
consistent with the Poisson distribution. The case of real networks does
not show the degree of most nodes is around \<k\> but has a power law
degree distribution with fat tailed and hubs. The property is called
'scale-free'. As shown in Figure 1 and Figure 2, "distances in a
scale-free network are smaller than the distances observed in an
equivalent random network". Hubs affect the extent of small worlds. The
more pronounced hubs are, the shorter the average path length is. With
the variance of γ (degree exponent), there are four stages of small
world.

-   Anomalous Regime (γ = 2), all nodes are close to each other by
    connecting to the central hub.

-   Ultra-Small World (2 ‹ γ ‹ 3), the hubs significantly reduce the
    path length. It occurs in many real social networks because of the
    broad degree distribution and the existence of hubs. A reference of
    figure 3.6, the peak value of five in Twitter and 3 in Wikipedia.

-   Critical Point (γ = 3), the path lengths shrink, compared to a
    random network of similar size.

-   Small World (γ \> 3), average path length is approximately same as
    the random small world networks. There are no large and numerous
    hubs to affect the average path length.

Figure 1 The degrees of a random network follow a Poisson distribution.
Most nodes have comparable degrees and nodes with a large number of
links are absent.

![Diagram Description automatically
generated](./images/media/image1.png){width="2.8419127296587927in"
height="2.475214348206474in"}

Source: Network Science, by Albert-Lászl 1

Figure 2 In a network with a power-law degree distribution most nodes
have only a few links.

![Diagram Description automatically
generated](./images/media/image2.png){width="2.850247156605424in"
height="2.6002252843394578in"}

Source: Network Science, by Albert-Lászl 2

## **Social network research in epidemics**

Humans have been fighting epidemics since the fourteenth century.
Epidemic pathogens spread on the physical contact network. The network
science-based analysis and prediction of epidemics has advanced for
decades, during which a robust analytical framework and the realization
of mobility networks are two breakthroughs.

The advance in technology gives us the ability to map out the network. A
robust analytical and numerical framework has been developed by
epidemiologists to quantify, analyse, and forecast the spread of
infectious diseases. At the early stage, based on two hypotheses
(compartmentalization and homogenous mixing), three basic models (SI,
SIS, SIR) are developed. Three models can demonstrate different dynamics
of a virus spreading according to the characteristics of infections.
Although an exponent growth can be seen in the first stage (Exponential
Regime) of all the three models, the three models have different results
in the next stage (Final Regime). In the SI model, everyone is infected
at the end. In the SIS model, the infection either remains a certain
fraction or dies out. In the SIR model, everyone recovers in the end. In
SIS and SIR, the basic reproduction number (R0) is a ratio, depending on
the infection rate, the recovery rate, and the average degree, that
determines the trend of epidemics to be either a major fraction is
infected, or the epidemic is mitigated. For example, the basic
reproduction number (R0) for measles is between 12 and 18, and for Ebola
is around 1.8 (Barabási, 2014; Menczer et al., 2020).

The real spreading network is a lot different from basic models. The two
hypotheses are false. The real network is scale-free, and individuals
tend to only contact the people they often contact. Additionally,
because the research of cure and vaccination takes years,
non-pharmaceutical interventions, such as quarantine, need to be taken.
Therefore, the timing and magnitude of interventions are very important,
and this depends on the accurate estimate of the infected population.
The revised model considers the compartment by degrees and the impact of
contact network topology. In the revised SI mode, spreading dynamics is
finite and is similar to random network for scale-free networks with
degree exponent γ≥3, while for scale-free networks with γ≤3 the spread
is instantaneous, because the hubs play the role in broadcasting the
disease fast to the rest of the network. Then as the high propagation
speed, the characteristic time vanishes. The outcome is heterogenous
networks enhance the spreading speed of the virus, even a weakly
infectious disease can spread fast. Figure 3 shows that nodes with
higher degrees are infected faster.) Similarly, in the revised SIS
model, in scale-free networks epidemic threshold vanishes. It leads a
virus with any spreading rate to be able to persist in the population.
Another result is zero characteristic time, the virus can reach every
node instantaneously. This also results from the impact of hubs.
Therefore, hubs with a very large degree are a game-changer. Once they
are infected, they become super-spreaders to propagate the disease
faster and further (Barabási, 2014; Menczer et al., 2020).

Figure 3 Fraction of Infected Nodes in the SI Model

![A picture containing histogram Description automatically
generated](./images/media/image3.png){width="3.8753794838145232in"
height="2.991418416447944in"}

Source: Network Science, by Albert-Lászl 3

To justify the theory that the speed of virus spreading depends on the
degree distribution of the relevant contact work, one study on a
sexually transmitted diseases contact network was conducted by
interviewing HIV patients. A scale-free property (power-law
distribution) is found. Most people have fewer sexual partners while a
few people have many sexual partners. The result is a lower epidemic
threshold and characteristic time. It ever first shows the empirical
evidence of the relation between scale-free property and the spreading
of infectious diseases. (Barabási, 2014; Menczer et al., 2020).

There are more factors to enhance the epidemics models. Some factors
increase the spreading, while some decrease the spreading.

-   **Temporal factor.** Most interactions occur in a short interevent
    time, and a few interactions occur in a long interval time. That
    predicts a slow decay time of the virus.

-   **Degree correction due to assortativity.** The assortativity
    decreases the epidemic threshold and accelerates the spreading. In
    SIR, the assortativity prolongs the epidemics and dimmish the
    prevalence.

-   **Contact duration and community structure.** The weight of links
    represents contact duration. Community structure shows strong ties
    in a community and weak ties between communities. The infection is
    slower, and the virus is more trapped within the local community
    other than spreading across communities.

In addition, immunization strategies are a valuable research field. The
target of immunization is to reduce the spreading rate under the
threshold. However, in a scale-free network, the epidemic threshold
vanishes. So, the spreading rate could not be reduced under the
threshold. The immunization strategy must be adjusted due to the
consideration of the factors from the network topology. The result is in
a random network, a high proportion of random immunization can protect
the uninfected people and decrease the spreading rate. In a scale-free
network with γ \< 3, if random immunization is applied, almost 100% of
people need to be immunized. Instead, immunization on hubs can increase
the threshold in heterogeneous networks. Around 30% immunization rate is
sufficient for a selective immunization strategy.

Furthermore, epidemic prediction is a challenging subject. Powerful
simulators can solve the problem. Behind the simulators is demographic
and human mobility data as inputs, and models with various algorithms.
For that, network science plays a vital role in the simulation.

Finally, the functions of mobility networks and effective distance has
been recognized in epidemic research. While in the past a virus needs to
take years to spread over a continent, now with global travelling,
viruses can easily reach any country within several days. Hence,
physical distance is replaced with effective distance. The larger
fraction of individuals moving between two locations, the shorter the
effective distance is. During a pandemic, the speed (arrival time) of
the pathogen is determined by two pathogen parameters: reproduction
rate, recovery rate, and one mobility network topology: mobility rate.
When pathogen parameters are unknown at the beginning, to estimate
relative arrival time, mobility rate is more important. Effective
distance is correlated with arrival time (Barabási, 2014; Menczer et
al., 2020).

## **Applications of network science in COVID-19 containment**

There are wide practices of network science in the Covid-19 pandemic.
Around the 'small world' concept, the content below will talk about the
case curve and distribution first, then talk about flatting the curve in
the small world network, next list containment measurements based on
analysis of network structures, and finally show available optimized
models.

Ray (2020) explored the small world phenomenon in the Covid-19 pandemic.
The article indicated that the Covid-19 case number grew very quickly
but did not do as quickly as an exponential growth due to the impact of
the network structure. As the explanation from the graph theory, the
degree distribution is power-law (scale-free). The connectedness between
nodes decreases gradually. Most people only contact a few people
(neighbours) in their communities. The case number changed as an initial
exponential growth followed by a fat-tail. To sum up, two phenomena
regarding small-world were 1) power-law growth in case number and
fatality, and 2) power-law distribution of cases in geographic areas.

Komarova et al. (2020) showed enhanced evidence for power-law growth in
case numbers. Epidemiological data from 174 countries depicted that in
the early stage, exponential growth occurred, but in the longer term, it
tended to be a power law. The trend was rooted in the absence of global
mixing in the spatial distribution of the contact network. The result is
supported by computer simulations. More, Xenikos and Asimakopoulos
(2021) suggested that in all European countries, in the diffusion phase
there was a uniform power-law growth in death rate with different
exponents, even if different mitigation interventions were called for.

As for power-law distribution of Covid-19 cases, Blasius (2020) found a
macro-epidemiological pattern through an analysis of confirmed cases and
death in worldwide countries and counties in the US. The pattern in
geography is a truncated power-law distribution with five orders of
magnitude. It is based on two facts: large-scale spread across countries
and small-scale accumulation in a country. There are huge differences in
case numbers between countries and areas in a country. The reason is a
heterogeneous network. The theory is confirmed by a simulation with a
meta-population model. In addition, Ahundjanov et al. (2022) conducted a
study that focuses on the first wave in China cities. A power law
distribution is found too. A few cities have a huge number of cases.

Since the outbreak of Covid-19, governments have realized the value of
the analysis of network structure with a small-world property on
containment and mitigation policies. Through an analysis of the South
Korea Covid spreading network, Jo et al. (2021) indicated that firstly
the non-pharmaceutical intervention such as social distancing could be
less effective because it is not based on the analysis of social network
structure. It is only a commonly used approach. Secondly, the production
of R0 does consider network influence. So, it is less reliable.
Outbreaks could be different even under the same R0. Eventually, they
concentrated on out-degree distribution. In a simulation, the removal of
top out-degree nodes can reduce the case number. This case highlighted
the importance of network structure analysis. Block et al. (2020)
focused on flatting the curve by removing the small-world character of
contact networks. Conventional way, restriction of social contact, aims
to decrease the height of the curve and spread it over a longer period
by reducing R0 but it causes isolation fatigue and increases costs of
quarantine. Whereas network-based strategy is more understandable and
feasible for individuals. The relationship between infection curve and
network distance should be investigated first. Then, the strategy takes
some steps to increase clusters and reduce shortcuts, including the
removal of the links between dissimilar nodes and nodes not in a
triangle or four-cycle, and the reduction of the number of contacts to
distinguish bubbles. Finally, the network is disconnected.

Some network models specifically for Covid-19 have been built to aid
governments in policy-making. Du (2021) pointed out the drawbacks of
continuous deterministic models and scale-free network models in
Covid-19 and claimed that the small-world network model is superior
because of the high clustering and low separating, which is the more
important character than degree distribution in Covid infection. In this
model, six states (susceptible, infected but not yet infectious,
symptomatically infectious, asymptomatically infectious, recovered,
deceased) are defined. Community and cross-community transmission occur
on contacts represented by regular links and random links respectively.
A series of graphs were made to show the impact of interventions and
reopening events. The result suggested that in the small world model the
infection is slower and less severe (the curve is flatter, and the peak
is lower).

Zhao (2020) built a model with a weighted graph. The model parameter is
obtained from China, validated in Italy, and applied in the US. In this
model, case isolation decreases the degree of infected nodes, quarantine
decreases the degree of nodes connected to infected nodes, and universal
precautions such as wearing masks reduce the probability of transmission
(the weight of a link). As the intervention, the number of links is
decreased, R0 is lowered, and then the transmission is reduced. Its
suggestion to the US is to limit the average degree to 7 each week and
then the average distance is increased to 10. If the new case decline,
the restriction is lifted gradually.

Karaivanov (2020) suggested that while a standard SIR model considers
the interaction between community members, heterogeneity, super spreader
and clusters, a network augmented model encompasses the effect of
non-pharmaceutical policies (herd immunity, distancing, lockdown,
testing, quarantine, and contact tracing), lifting and imposing time,
and people's behavioural responses. Economic parameters including
people's savings, employment status and ability to pay bills and rents
were added to the dynamics.

Li et al. (2021) suggested a SEIAR model based on a small world network,
including five infection states, and featuring latent period and
asymptomatic infection. This study recognized the feasibility and
effectiveness of current non-pharmaceutical interventions and the
importance of measurement timing at different stages. It also pointed
out that the drawback of the previous models is ignorance of the
underlying network and its heterogeneity. As the cost of lockdown
increases, isolating hubs is more effective.

## **Implication for governments to contain Covid-19**

The advance of network science and the emergence of network augmented
Covid-19 models bring implications for governments to effectively
contain Covid-19. The power of government measurements to combat virus
spreading has been recognised in academics.

First of all, moderate, cost-effective measurements are expected to be
adopted. the feasibility and effectiveness of non-pharmaceutical
interventions are recognized, especially before the effective vaccine
and drug are available. However, at the same time, the adverse impact of
these policies on the economy, society and psychology is seen. Thus,
moderate, cost-effective measurements are appealed. Intervention
timeliness and targeted group are critical to achieving the goal.
Isolating and vaccinating hubs is proved to be more effective. It can
increase distances and reduce transmission in communities. Long-range
infections should be drawn attention to because they reduce distances
and cause cross-community outbreaks. As the curve passes the peak, the
restriction should be lifted gradually. At the same time, people in
different infection states should be treated by different measurements.
For example, bring infected cases to medical facilities, moderate to
server cases to hospital, and mild cases to be quarantined.

In addition, a good understanding of the geographic and demographic
differences between areas can help governments better use resources and
design policies. Policies should vary from metropolitans with dense
populations to small places with sparsely populated. In addition, the
human subjective conscious plays an important role in combating the
virus. The impact of ethical groups and genders on clustering is not
supposed to be ignored. In these aspects, social network analysis can be
applied to visualize and analyse these characteristics so as to take
effective spreading-control actions.

Moreover, the use of network analysis contact tracing tools can monitor
and control outbreaks. Contact tracing tools are used to collect data,
and network analysis tools are applied to create graphs. With the
creation of static and real-time maps, the properties r of contact
networks, hotspots and key actors are visible, as shown in Figure 4.
Further actions can be taken to effectively contain the virus.

Figure 4 Network analysis by sources of infection (Cytoscape). Node size
determined by betweenness. Arrowheads indicate direction of transmission
from source

![A picture containing diagram Description automatically
generated](./images/media/image4.png){width="5.768055555555556in"
height="4.165972222222222in"}

Source: Saraswathi et al., 2020

## **Conclusion**

Although small world phenomenon originates from random networks, small
world property is noticeable as the emergence of hubs in real networks.
And it has been an influential property in real social networks, and
thus distances between two individuals become even shorter than 'six
degrees of separation'. Based on small world property and other
properties and assumptions, epidemiologists have established a robust
analytical framework. The framework encompasses a variety of models.
Integrated with mobility networks, augmented models can make epidemic
prediction more accurate and immunization strategies targeted and
efficient. Small world property leads to power-law Covid-19 case curve
and distribution. Varied Covid-19 models also help governments to the
make right policies and non-pharmaceutical interventions to flat the
curve. The function of network science in Covid-19 data collection,
simulation, and prediction is significant.

**\
**

## **References**

Ahundjanov, B. B., Akhundjanov, S. B., & Okhunjanov, B. B. (2022). Power
law in COVID‐19 cases in china. Journal of the Royal Statistical
Society. Series A, Statistics in Society, 185(2), 699-719.
https://doi.org/10.1111/rssa.12800

Barabási, A. L. (2014). Network science book. Network Science, 625.

Blasius, B. (2020). Power-law distribution in the number of confirmed
COVID-19 cases. *Chaos (Woodbury, N.Y.), 30*(9), 093123-093123.
https://doi.org/10.1063/5.0013031

Block, P., Hoffman, M., Raabe, I. J., Dowd, J. B., Rahal, C., Kashyap,
R., & Mills, M. C. (2020). Social network-based distancing strategies to
flatten the COVID-19 curve in a post-lockdown world. *Nature Human
Behaviour, 4*(6), 588-596. https://doi.org/10.1038/s41562-020-0898-6

Du, M. (2021). Mitigating COVID-19 on a small-world network. *Scientific
reports, 11*(1), 1-9.

Jo, W., Chang, D., You, M., & Ghim, G. (2021). A social network analysis
of the spread of COVID-19 in south korea and policy implications.
Scientific Reports, 11(1), 8581-8581.
https://doi.org/10.1038/s41598-021-87837-0

Karaivanov, A. (2020). A social network model of COVID-19. *PloS One,
15*(10), e0240878-e0240878. https://doi.org/10.1371/journal.pone.0240878

Komarova, N. L., Schang, L. M., & Wodarz, D. (2020). Patterns of the
COVID-19 pandemic spread around the world: Exponential versus power
laws. *Journal of the Royal Society Interface, 17*(170),
20200518-20200518. https://doi.org/10.1098/rsif.2020.0518

Li, J., Zhong, J., Ji, Y., & Yang, F. (2021). A new SEIAR model on
small-world networks to assess the intervention measures in the COVID-19
pandemics. *Results in Physics, 25*, 104283.
https://doi.org/10.1016/j.rinp.2021.104283

Menczer, F., Fortunato, S., & Davis, C. A. (2020). A first course in
network science. Cambridge University Press.

Ray, T. (2020, March 17). *Graph theory suggests COVID-19 might be a
'small world' after all*. ZDNet.
https://www.zdnet.com/article/graph-theory-suggests-covid-19-might-be-a-small-world-after-all/

Saraswathi, S., Mukhopadhyay, A., Shah, H., & Ranganath, T. S. (2020).
Social network analysis of COVID-19 transmission in Karnataka, India.
*Epidemiology & Infection, 148*.

Xenikos, D. G., & Asimakopoulos, A. (2021). Power-law growth of the
COVID-19 fatality incidents in europe. *Infectious Disease Modelling,
6*, 743-750. https://doi.org/10.1016/j.idm.2021.05.001

Zhao, P. J. (2020). A social network model of the COVID-19 pandemic.
*MedRxiv*.
