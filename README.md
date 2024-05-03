RealEstate Tenant Register Complaint (Website)
--------------------------

**1. Tenant Complaint Register View.**

<img src="assets/images/websiteview1.png">

* **Tenant Name :-** Name Of Tenant.
* **Email :-** Registered Tenant Email Enter valid email for smoother communication.
* **Address :-** Tenant (aprtment, flat, ...) Address.
* **Type :-** Complaint Type (Ex. Heating issue, Water, Question ..etc)
* **Description :-** Describe the problem in detail, If **Question** then describe question.

By Clicking Submit button complaint will be submited.
-

**2. Thank You Page.**

<img src="assets/images/websiteview2.png">

- Once Complaint is registered displays thank you page and **complaint number**.


RealEstate Tenant Register Complaint (Backend)
-

**1. Admin Panel Complaint View.**

<img src="assets/images/backendview.png">

* If complaint registered tenant get **complaint email** and with **complaint number** on email.
* if type is **Question**, **Answer Complaint** button visible.
* Admin Directly drop complaint by **DropComplaint** button.

**2. Answer Complaint View.**

<img src="assets/images/backendview1.png">

* Give answer to complaint and directly close complaint.

**3. Solved Answer Complaint View.**

<img src="assets/images/backendview2.png">

* Once complaint closed with answer it wil **send mail to tenant with answer** and representative can see details **solved date** and **reason**.

**4. Complaint View (Type not question).**

<img src="assets/images/backendview3.png">

* Complaint type is not **Question** so here **Classify Complaint** button visible.
* And representative note down **Action Plan** for the complaint.

**5. Complaint View (In Review State)**

<img src="assets/images/backendview4.png">

* In this state, representative classify complaint with action plan using **Classify with action plan** button.
* representative need to write down **ActionPlan(Required)**.

**6. Complaint View (In Progress State)**

<img src="assets/images/backendview5.png">

* Once Classify Complaint Done representative can **resolve** complaint.

**7. Complaint View (Resolved State)**

<img src="assets/images/backendview6.png">

* Once representative **resolve** complaint a **mail send to tenant** with taken **actionplan** taken for solve complaint.
* in **Resolve Details** Section representative can see details of resolve reason and date.