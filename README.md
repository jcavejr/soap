# soap

## Inspiration

Social media has become an inseparable aspect of life but yet we often neglect the significance of joining this open network. Bad decisions and posts can haunt in the future in job search, scholarships and other endeavors, however people can sometimes be unaware that their posts contain controversial or harmful content. Hence, we wanted to make a program that can analyze one's appearance to the public based on past activity so people can be aware about how it is and decide if they want to change in the future or delete things from the past.

## What it does

Analyzes the user's tweets and gives statistics showing how many of the tweets may come off in a negative way. It is meant to guide the user to make less controversial posts in the future or to get rid of some past dangerous posts.

## How I built it

Google cloud language and key "bad words" are used to judge how negative the tweets taken from the Twitter API seem. Swift was then used to create a nicely formatted iOS app for users to see statistics about their Tweets.

## Challenges I ran into

At first we tried to use AWS to host the database of user's negative Tweets. It turned out to be extremely difficult to get the iOS app to link to the database, so we scratched that idea. We did learn a lot about using AWS databases though.

Additionally, we tried to make a chrome extension to warn users before making negative posts but it turned out to be too complicated to interact with text inside of text boxes.

Finally, the Twitter library for iOS was difficult to use. Instead we ended up getting the statistics in Python and feeding that data to the iOS app.

## What I learned

   * AWS DyamoDB
   * Google Cloud Language API
   * Twitter API with Tweepy
   * Firebase
   * iOS
   * Chrome Extensions

## What's next for S.O.A.P

   * A chrome extension to warn you before you send something that might hurt you in the future.
   * Integrating with other social media platforms like Facebook and Instagram

