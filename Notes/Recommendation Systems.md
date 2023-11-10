---
tags:
  - programming-level-1
  - y2023
  - slss
  - notes
---
# Systems

## Popularity and Likes

This type of paradigm makes a suggestion based on how many people like the thing.

One prime example of this is the like button (heart) in Instagram. When you click that heart, Instagram records it and based on information it has on you, it might suggest that to someone else that is similar to you.

We created the Favourite Bubble Tea service, which is based on the "Popularity/Likes" paradigm of recommendation systems.


## N-Point Rating System

N-Point rating systems are used by many services, but one that nearly everyone is familiar with is Amazon's main purchasing service.

This paradigm is where users rate a product out a certain number.


## Similarity Scores

Amazon, Netflix, and Meta all use Similarity Scores to help drive users to their platform.

> Example:
> Ubial likes ["nintendo switch", "usb chargers", "4k blue ray movies]
> Ben Ubial likes ["nintendo switch", "usb chargers", "lego"]
> Fido likes ["lego", "chew toys", "dog food"]

Similarity score between Ubial and Ben Ubial: 2
Similarity score between Ubial and Fido: 0
Similarity score between Ben Ubial and Fido: 1