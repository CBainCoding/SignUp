<h3>Project overview</h3>
This is a website designed for users to be able to sign up with an account that is then visible to admins. Users can create, view their account details, edit and delete their account all from the front-end. There is an FAQs page which ordinary users can access while staff-level users can again, create, edit and delete FAQs from the front end. Once users log in they can send in an enquiry which is visible to admins in the back-end and is tied to a user account.

The initial purpose of the site was to act as a store for club officers to have access to member details, with the members able to edit details themselves rather than requiring the club officers to update. During testing several users felt that the creating account process did not deliver any real benefit to them and so the "Enquiries" app was added to give logged in users a way to message the club admins.

<h3>List of features</h3>

- __Navbar__
    - The Navbar shows links to all site pages and updates to show different buttons when logged in, the "Login/Signup" button is a dropdown that when clicked offers both a "Login" and "Create Account" button. When a user is logged in the "Login/Signup" button switches to a "Log out" button.
    - During user testing some users had difficulty reading the font due to the text colour, this was therefore changed to a brighter off-white colour to improve readability.
    - The Navbar is part of the base.html file and as all other html files extend this base.html, the Navbar remains consistent across the site.
    - On smaller devices the Navbar collapses and can be opened with the burger icon and continues the difference in links shows depending on whether the user is logged in
    </br>
    ![Navbar](static/media/readme_images/Navbar.png)
    </br>
    ![Navbar](static/media/readme_images/NavbarLoggedIn.png)
    </br>
    ![Navbar_Collapsed](static/media/readme_images/NavbarCollapsed.png)
    ![Navbar_Collapsed](static/media/readme_images/NavbarCollapsedLoggedIn.png)

- __FAQs__
    - The FAQs page allows users to see commonly asked questions about the club without the need to bother the club officers.
    - Club officers with staff accounts have a front-end form that allows them to add, edit and delete FAQs from this page.
    - Django messaging system used to confirm new and edited FAQs. During testing the "Delete" message does not appear which requires further investigation.
    - Confirmation page for deleting FAQs to try and avoid accidental deletions.
    </br>
    ![FAQs_Page](static/media/readme_images/FAQs_page.png)
    ![Staff_FAQs](static/media/readme_images/Staff_FAQs.png)
    ![FAQs_Messages](static/media/readme_images/Edit_FAQ_Message.png)
    ![Delete_FAQ_Confirm](static/media/readme_images/Delete_FAQ_confirmation.png)


- __Contact__
- __User Accounts__

- __Future features__
- Currently the club staff have no way to access the enquiries unless given permission by the admin/superuser. I would like to add an "inbox" page that displays the enquiries in a front-end page so that staff do not need to access the admin panel.

<h3>UX/UI</h3>



<h3>Testing</h3>

All pages forms have been tested and create relevent instances in the back-end. For users they can see their account through the front-end "My Account" page, staff level users can also add new FAQs to the FAQs page, as well as editing and deleting from the front-end. One bug that was found was during the "Delete Account" process the message to confirm account deletion does not display while the create and edit messages do. This requires futher investigation.

All html pages have been run through the official [W3C validator](https://validator.w3.org/). This was done by right clicking on each page and viewing source, then pasting into the validator. All pages have been tested both not logged in and logged in. For pages such as the FAQs where staff can see additional features, an additional test was performed with a staff account logged in.

CSS stylesheet has passed the official [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) with no errors.
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

All modified .py files have been run through the [Code Institute linter](https://pep8ci.herokuapp.com/). A lot of the code did not confirm to PEP8 standards so was reformatted correctly to meet these requirements and now passes with no errors.

All site pages and forms have been tested on multiple devices from large desktop monitors to mobile phones. The pages and forms aldisplay correctly. Styling could be improved on some forms such as the enquiry form but this was pushed to a "Should do" requirement as the current styling meets MVP requirements.

<h3>Deployment</h3>

<h3>Citation of ALL sources(code, images, text)</h3>

<h3>Future features </h3>

<h3>Known Bugs</h3>
Delete FAQ message not showing when a user deletes from the front-end. For some reason while the messages work when creating and editing the FAQs page, the delete message does not show.
Same email address is allowed on multiple accounts when signing up. This can be solved but was left as it is for users signing up as some club members may sign themselves and their children up on different accounts